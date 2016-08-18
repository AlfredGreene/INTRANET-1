from decouple import config
import pypyodbc
import datetime
import json

def bwt_report(args,kwargs):

    def sql_conn(arg):
        conn = config('TOPSHOP_BWT')
        connection = pypyodbc.connect(conn)
        cursor = connection.cursor()
        SQLCommand =(arg)
        cursor.execute(SQLCommand)
        results = cursor.fetchone()
        lista = [results]
        while results:
            # print('[%s-%s]' % (str(results[0]), str(results[1])) )
            results = cursor.fetchone()
            lista.append(results)
        connection.close()

        return lista

    def get_department():

        SQLCommand = ('SELECT DESCRIPCION, CODLINEA FROM LINEA ORDER BY CODLINEA')
        department = sql_conn(SQLCommand)
        return department


    def get_department_sub(department):

        SQLCommand = ('''
        SELECT MAX(LN.DESCRIPCION)AS Lina,
        max( ARCL.DESCRIPCIONDEPTO)AS Descripcion
        FROM
        ALBVENTALIN AVL inner join ALBVENTACAB AVC on AVL.NUMALBARAN = AVC.NUMALBARAN
        AND AVL.NUMSERIE = AVC.NUMSERIE
        inner join ARTICULOS AR on AVL.CODARTICULO = AR.CODARTICULO
        inner Join DEPARTAMENTO D on AR.DPTO = D.NUMDPTO
        inner join LINEA LN on AR.LINEA = LN.CODLINEA
        inner join ARTICULOSCAMPOSLIBRES ARCL on AR.CODARTICULO = ARCL.CODARTICULO
        WHERE
        LN.DESCRIPCION = '{department}'
        Group by AR.DPTO, D.NUMDPTO
        ORDER BY Descripcion'''.format(department=department))
        department_sub = sql_conn(SQLCommand)
        return department_sub


    def get_report(date1,date2,department,department_sub):

        SQLCommand = ("""SELECT  MAX(D.DESCRIPCION) AS CodDpto ,MAX(LN.DESCRIPCION) AS Lina, MAX(ARCL.DESCRIPCIONDEPTO) AS Descripcion, SUM(AVL.UNIDADESTOTAL) AS ActBrUnit, SUM(AVL.TOTAL - (AVL.TOTAL*(AVC.DTOCOMERCIAL/100))) AS ActBr
        ,(SUM(AVL.TOTAL)/(Select Sum(v.TOTAL - (v.TOTAL*(c.DTOCOMERCIAL/100)))
        From ALBVENTALIN v
        inner join ALBVENTACAB c on v.NUMALBARAN = c.NUMALBARAN
                               AND v.NUMSERIE = c.NUMSERIE
        where v.NUMSERIE Like 'FG%'
        and convert(varchar(10), c.FECHA,23) between '{date1}' and '{date2}')) * 100 as [BrSls]
        ,MAX(D.AREA) AS ActFt
        ,Case When MAX(D.AREA) <> 0 Then SUM(AVL.TOTAL - (AVL.TOTAL*(AVC.DTOCOMERCIAL/100)))/MAX(D.AREA) else '0' end as [BrFt]
        From ALBVENTALIN AVL
        inner join ALBVENTACAB AVC on AVL.NUMALBARAN = AVC.NUMALBARAN AND AVL.NUMSERIE = AVC.NUMSERIE
        inner join ARTICULOS AR on AVL.CODARTICULO = AR.CODARTICULO
        inner Join DEPARTAMENTO D on AR.DPTO = D.NUMDPTO
        inner join LINEA LN on AR.LINEA = LN.CODLINEA
        inner join ARTICULOSCAMPOSLIBRES ARCL on AR.CODARTICULO = ARCL.CODARTICULO
        Where AVL.NUMSERIE Like 'FG%'
        and convert(varchar(10), AVC.FECHA,23) between '{date1}' and '{date2}'
        and LN.DESCRIPCION = '{department}'
        and ARCL.DESCRIPCIONDEPTO = '{department_sub}'
        ORDER BY CodDpto""".format(date1=date1,date2=date2,department=department,department_sub=department_sub))
        report = sql_conn(SQLCommand)
        return report


    def get_stock(department,department_sub):

        SQLCommand = ("""SELECT  MAX(D.DESCRIPCION) AS CodDpto
        ,MAX(LN.DESCRIPCION) AS Lina
        ,MAX(ARCL.DESCRIPCIONDEPTO) AS Descripcion
        ,SUM(STK.STOCK) AS ActBrUnits
        ,SUM(STK.STOCK * CXA.ULTIMOCOSTE) AS ActBr
        ,(SUM(STK.STOCK * CXA.ULTIMOCOSTE) / (Select Sum(s.STOCK * c.ULTIMOCOSTE)
                           From  ARTICULOSLIN l
                           inner join STOCKS s on l.CODARTICULO = s.CODARTICULO AND l.TALLA = s.TALLA AND l.COLOR = s.COLOR
                           inner join COSTESPORALMACEN c on l.CODARTICULO = c.CODARTICULO AND l.TALLA = c.TALLA AND l.COLOR = c.COLOR
                           where  s.CODALMACEN = 'PB1'
                              and c.CODALMACEN = 'PB1') * 100) AS [BrStk]
        From ARTICULOSLIN AL
        inner join STOCKS STK on AL.CODARTICULO = STK.CODARTICULO AND AL.TALLA = STK.TALLA AND AL.COLOR = STK.COLOR
        inner join COSTESPORALMACEN CXA on AL.CODARTICULO = CXA.CODARTICULO AND AL.TALLA = CXA.TALLA AND AL.COLOR = CXA.COLOR
        inner join ARTICULOS AR on AL.CODARTICULO = AR.CODARTICULO
        inner Join DEPARTAMENTO D on AR.DPTO = D.NUMDPTO
        inner join LINEA LN on AR.LINEA = LN.CODLINEA
        inner join ARTICULOSCAMPOSLIBRES ARCL on AR.CODARTICULO = ARCL.CODARTICULO
        Where STK.CODALMACEN = 'PB1'
        and CXA.CODALMACEN = 'PB1'
        and LN.DESCRIPCION = '{department}'
        and ARCL.DESCRIPCIONDEPTO = '{department_sub}'
        Group by AR.DPTO, D.NUMDPTO""".format(department=department,department_sub=department_sub))
        stock = sql_conn(SQLCommand)
        return stock


    '''
    Vars
    '''
    department = get_department()
    department.remove(None)

    # User Comparision date
    # Actual dates
    # act_date_from = '2016-07-03'
    act_date_from = args
    # act_date_to = '2016-07-09'
    act_date_to = kwargs
    # Last week dates
    lw_date_from_c = datetime.datetime.strptime(act_date_from, "%Y-%m-%d") - datetime.timedelta(weeks=1)
    lw_date_from = '{:.10}'.format(str(lw_date_from_c.isoformat()))
    lw_date_to_c = datetime.datetime.strptime(act_date_to, "%Y-%m-%d") - datetime.timedelta(weeks=1)
    lw_date_to ='{:.10}'.format(str(lw_date_to_c.isoformat()))

    actbr_u = 0
    actbr_u_total = 0
    actbr_u_total_total = 0
    actbr_val = 0
    actbr_val_total = 0
    actbr_val_total_total = 0
    pinbr_val = 0
    pinbr_val_total = 0
    pinbr_val_total_total = 0
    pinbr_per = 0
    pinbr_per_total = 0
    pinbr_per_total_total = 0
    pin_market_per = 0
    pin_market_per_total = 0
    pin_market_per_total_total = 0
    lwbr_val = 0
    lwbr_val_total = 0
    lwbr_val_total_total = 0
    lwbr_per = 0
    lwbr_per_total = 0
    lwbr_per_total_total = 0
    lw_market_per = 0
    lw_market_per_total = 0
    lw_market_per_total_total = 0
    lybr_val = 0
    lybr_val_total = 0
    lybr_val_total_total = 0
    lybr_per = 0
    lybr_per_total = 0
    lybr_per_total_total = 0
    ly_market = 0
    ly_market_total = 0
    ly_market_total_total = 0
    w_lift_req = 0
    w_lift_req_total = 0
    w_lift_req_total_total = 0
    brsls = 0
    brsls_total = 0
    brsls_total_total = 0
    br_stk = 0
    br_stk_total = 0
    br_stk_total_total = 0
    br_space = 0
    br_space_total = 0
    br_space_total_total = 0
    market_sls = 0
    market_sls_total = 0
    market_sls_total_total = 0
    market_stk = 0
    market_stk_total = 0
    market_stk_total_total = 0
    market_space = 0
    market_space_total = 0
    market_space_total_total = 0
    act_ft = 0
    act_ft_total = 0
    act_ft_total_total = 0
    br_ft = 0
    br_ft_total = 0
    br_ft_total_total = 0
    market_ft = 0
    market_ft_total = 0
    market_ft_total_total = 0
    stok_actbr_u, stok_actbr_u_total, stok_actbr_u_total_total = 0,0,0
    stok_br_u, stok_br_u_total, stok_br_u_total_total = 0,0,0
    stok_actbr_cover,stok_actbr_cover_total,stok_actbr_cover_total_total = 0,0,0
    stok_act_market_cover,stok_act_market_cover_total,stok_act_market_cover_total_total = 0,0,0
    i,n,a = 0,0,1

    '''
    fin
    '''


    # # Obtain the descripcion
    # descripcion = get_description()

    report_values = {}
    report_values_total = {}
    report_values_total_total = {}
    dictionary = {}

    for i in range(len(department)):

        x = department[i][0]
        department_name = '-%s' % x
        department_sub = get_department_sub(x)
        department_sub.remove(None)
        dictionary[department_name] = [department_name]
        # a += a
        # report_json.append([x])
        for n in range(len(department_sub)):

            y = department_sub[n][1]
            department_sub_name = '-%s' % y
            department_sub_id = department_sub[n][0]

            # Obtain Actual data
            act_report = get_report(act_date_from,act_date_to,x,y)
            act_report.remove(None)

            # Obtain Last Week data
            lw_report = get_report(lw_date_from,lw_date_to,x,y)
            lw_report.remove(None)

            # Obtain STOCKS
            stock_report = get_stock(x,y)
            stock_report.remove(None)

            actbr_u = act_report[0][3]
            if actbr_u == None:
                actbr_u = 0
            else:
                actbr_u = int(actbr_u)

            actbr_val = act_report[0][4]
            if actbr_val == None:
                actbr_val = 0
            else:
                actbr_val = actbr_val

            lwbr_val_c = lw_report[0][3]
            if lwbr_val_c == None:
                lwbr_val_c = 0
            else:
                lwbr_val_c = lwbr_val_c

            lwbr_val = actbr_u - lwbr_val_c
            if lwbr_val == 0:
                lwbr_per = 0
            else:
                lwbr_per = ((actbr_val/lwbr_val)*100)
                lwbr_per = lwbr_per

            brsls = act_report[0][5]
            if brsls == None:
                brsls = 0
            else:
                brsls = int(brsls)

            br_stk = stock_report[0][5]
            if br_stk == None:
                br_stk = 0
            else:
                br_stk = int(br_stk)

            act_ft = act_report[0][6]
            if act_ft == None:
                act_ft = 0
            else:
                act_ft = int(act_ft)

            br_ft = act_report[0][7]
            if br_ft == None:
                br_ft = 0
            else:
                br_ft = br_ft

            stok_br_u = stock_report[0][3]
            if stok_br_u == None:
                stok_br_u = 0
            else:
                stok_br_u = int(stok_br_u)

            stok_actbr_u = stock_report[0][4]
            if stok_actbr_u == None:
                stok_actbr_u = 0
            else:
                stok_actbr_u = stok_actbr_u
            if lwbr_val == 0:
                stok_actbr_cover = 0
            elif actbr_val == 0:
                stok_actbr_cover = 0
            else:
                stok_actbr_cover = lwbr_val/actbr_val
                stok_actbr_cover = stok_actbr_cover

            # report_values[department_sub_name] ={
            #     "name":y,
            #     "actbr_u":actbr_u,
            #     "actbr_val":actbr_val,
            #     "pinbr_val":pinbr_val,
            #     "pinbr_per":pinbr_per,
            #     "pin_market_per":pin_market_per,
            #     "lwbr_val":lwbr_val,
            #     "lwbr_per":lwbr_per,
            #     "lw_market_per":lw_market_per,
            #     "lybr_val":lybr_val,
            #     "lybr_per":lybr_per,
            #     "ly_market":ly_market,
            #     "w_lift_req":w_lift_req,
            #     "brsls":brsls,
            #     "br_stk":br_stk,
            #     "br_space":br_space,
            #     "market_sls":market_sls,
            #     "market_stk":market_stk,
            #     "market_space":market_space,
            #     "act_ft":act_ft,
            #     "br_ft":br_ft,
            #     "market_ft":market_ft,
            #     "stok_br_u":stok_br_u,
            #     "stok_actbr_u":stok_actbr_u,
            #     "stok_actbr_cover":stok_actbr_cover,
            #     "stok_act_market_cover":stok_act_market_cover,
            # }
            report_values[department_sub_name]={
                # "11 name":department_sub_name,
                "12 actbr_u":actbr_u,
                "13 actbr_val":actbr_val,
                "14 pinbr_val":pinbr_val,
                "15 pinbr_per":pinbr_per,
                "16 pin_market_per":pin_market_per,
                "17 lwbr_val":lwbr_val,
                "18 lwbr_per":lwbr_per,
                "19 lw_market_per":lw_market_per,
                "20 lybr_val":lybr_val,
                "21 lybr_per":lybr_per,
                "22 ly_market":ly_market,
                "23 w_lift_req":w_lift_req,
                "24 brsls":brsls,
                "25 br_stk":br_stk,
                "26 br_space":br_space,
                "27 market_sls":market_sls,
                "28 market_stk":market_stk,
                "29 market_space":market_space,
                "30 act_ft":act_ft,
                "31 br_ft":br_ft,
                "32 market_ft":market_ft,
                "33 stok_br_u":stok_br_u,
                "34 stok_actbr_u":stok_actbr_u,
                "35 stok_actbr_cover":stok_actbr_cover,
                "36 stok_act_market_cover":stok_act_market_cover,
            }

            actbr_u_total += actbr_u
            actbr_val_total += actbr_val
            pinbr_val_total += pinbr_val
            pinbr_per_total += pinbr_per
            pin_market_per_total += pin_market_per
            lwbr_val_total += lwbr_val
            # lwbr_val_total = lwbr_val_total
            lwbr_per_total += lwbr_per
            # lwbr_per_total = lwbr_per_total
            lw_market_per_total += lw_market_per
            lybr_val_total += lybr_val
            lybr_per_total += lybr_per
            ly_market_total += ly_market
            w_lift_req_total += w_lift_req
            brsls_total += brsls
            br_stk_total += br_stk
            br_space_total += br_space
            market_sls_total += market_sls
            market_stk_total += market_stk
            market_space_total += market_space
            act_ft_total += act_ft
            br_ft_total += br_ft
            market_ft_total += market_ft
            stok_br_u_total += int(stok_br_u)
            stok_actbr_u_total += stok_actbr_u
            stok_actbr_cover_total += stok_actbr_cover
            stok_act_market_cover_total += stok_act_market_cover

            # report_values.dic({report_value})
        dictionary[department_name]=report_values

        report_values ={}
        w = 'TOTAL'
        report_values_total[w] ={
            # "11 name":w,
            "12 actbr_u_total":actbr_u_total,
            "13 actbr_val_total":actbr_val_total,
            "14 pinbr_val_total":pinbr_val_total,
            "15 pinbr_per_total":pinbr_per_total,
            "16 pin_market_per_total":pin_market_per_total,
            "17 lwbr_val_total":lwbr_val_total,
            "18 lwbr_per_total":lwbr_per_total,
            "19 lw_market_per_total":lw_market_per_total,
            "20 lybr_val_total":lybr_val_total,
            "21 lybr_per_total":lybr_per_total,
            "22 ly_market_total":ly_market_total,
            "23 w_lift_req_total":w_lift_req_total,
            "24 brsls_total":brsls_total,
            "25 br_stk_total":br_stk_total,
            "26 br_space_total":br_space_total,
            "27 market_sls_total":market_sls_total,
            "28 market_stk_total":market_stk_total,
            "29 market_space_total":market_space_total,
            "30 act_ft_total":act_ft_total,
            "31 br_ft_total":br_ft_total,
            "32 market_ft_total":market_ft_total,
            "33 stok_br_u_total":stok_br_u_total,
            "34 stok_actbr_u_total":stok_actbr_u_total,
            "35 stok_actbr_cover_total":stok_actbr_cover_total,
            "36 stok_act_market_cover_total":stok_act_market_cover_total,
        }
        # report_values_total[w] ={
        #     "name":w,
        #     "actbr_u_total":actbr_u_total,
        #     "actbr_val_total":actbr_val_total,
        #     "pinbr_val_total":pinbr_val_total,
        #     "pinbr_per_total":pinbr_per_total,
        #     "pin_market_per_total":pin_market_per_total,
        #     "lwbr_val_total":lwbr_val_total,
        #     "lwbr_per_total":lwbr_per_total,
        #     "lw_market_per_total":lw_market_per_total,
        #     "lybr_val_total":lybr_val_total,
        #     "lybr_per_total":lybr_per_total,
        #     "ly_market_total":ly_market_total,
        #     "w_lift_req_total":w_lift_req_total,
        #     "brsls_total":brsls_total,
        #     "br_stk_total":br_stk_total,
        #     "br_space_total":br_space_total,
        #     "market_sls_total":market_sls_total,
        #     "market_stk_total":market_stk_total,
        #     "market_space_total":market_space_total,
        #     "act_ft_total":act_ft_total,
        #     "br_ft_total":br_ft_total,
        #     "market_ft_total":market_ft_total,
        #     "stok_br_u_total":stok_br_u_total,
        #     "stok_actbr_u_total":stok_actbr_u_total,
        #     "stok_actbr_cover_total":stok_actbr_cover_total,
        #     "stok_act_market_cover_total":stok_act_market_cover_total,
        # }

        # dictionary[x] =
        dictionary[department_name].update(report_values_total)

        report_values_total = {}


        actbr_u_total_total += actbr_u_total
        actbr_val_total_total += actbr_val_total
        pinbr_val_total_total += pinbr_val_total
        pinbr_per_total_total += pinbr_per_total
        pin_market_per_total_total += pin_market_per_total
        lwbr_val_total_total += lwbr_val_total
        lwbr_per_total_total += lwbr_per_total
        lw_market_per_total_total += lw_market_per_total
        lybr_val_total_total += lybr_val_total
        lybr_per_total_total += lybr_per_total
        ly_market_total_total += ly_market_total
        w_lift_req_total_total += w_lift_req_total
        brsls_total_total += brsls_total
        br_stk_total_total += br_stk_total
        br_space_total_total += br_space_total
        market_sls_total_total += market_sls_total
        market_stk_total_total += market_stk_total
        market_space_total_total += market_space_total
        act_ft_total_total += act_ft_total
        br_ft_total_total += br_ft_total
        market_ft_total_total += market_ft_total
        stok_actbr_u_total_total += stok_actbr_u_total
        stok_br_u_total_total += stok_br_u_total
        stok_actbr_cover_total_total += stok_actbr_cover_total
        stok_act_market_cover_total_total += stok_act_market_cover_total
        """"""
        actbr_u_total ,actbr_val_total ,pinbr_val_total ,pinbr_per_total ,pin_market_per_total ,lwbr_val_total ,lwbr_per_total ,lw_market_per_total ,lybr_val_total ,lybr_per_total ,ly_market_total ,w_lift_req_total ,brsls_total ,br_stk_total ,br_space_total ,market_sls_total ,market_stk_total ,market_space_total ,act_ft_total ,br_ft_total ,market_ft_total ,stok_br_u_total ,stok_actbr_u_total ,stok_actbr_cover_total ,stok_act_market_cover_total = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    zzz = 'TOTAL TOTAL'
    # report_values_total_total[zzz] = {
    #     "name":zzz,
    #     "actbr_u_total_total":actbr_u_total_total,
    #     "actbr_val_total_total":actbr_val_total_total,
    #     "pinbr_val_total_total":pinbr_val_total_total,
    #     "pinbr_per_total_total":pinbr_per_total_total,
    #     "pin_market_per_total_total":pin_market_per_total_total,
    #     "lwbr_val_total_total":lwbr_val_total_total,
    #     "lwbr_per_total_total":lwbr_per_total_total,
    #     "lw_market_per_total_total":lw_market_per_total_total,
    #     "lybr_val_total_total":lybr_val_total_total,
    #     "lybr_per_total_total":lybr_per_total_total,
    #     "ly_market_total_total":ly_market_total_total,
    #     "w_lift_req_total_total":w_lift_req_total_total,
    #     "brsls_total_total":brsls_total_total,
    #     "br_stk_total_total":br_stk_total_total,
    #     "br_space_total_total":br_space_total_total,
    #     "market_sls_total_total":market_sls_total_total,
    #     "market_stk_total_total":market_stk_total_total,
    #     "market_space_total_total":market_space_total_total,
    #     "act_ft_total_total":act_ft_total_total,
    #     "br_ft_total_total":br_ft_total_total,
    #     "market_ft_total_total":market_ft_total_total,
    #     "stok_actbr_u_total_total":stok_actbr_u_total_total,
    #     "stok_br_u_total_total":stok_br_u_total_total,
    #     "stok_actbr_cover_total_total":stok_actbr_cover_total_total,
    #     "stok_act_market_cover_total_total":stok_act_market_cover_total_total,
    # }
    report_values_total_total[zzz] = {
        # "11 name":zzz,
        "12 actbr_u_total_total":actbr_u_total_total,
        "13 actbr_val_total_total":actbr_val_total_total,
        "14 pinbr_val_total_total":pinbr_val_total_total,
        "15 pinbr_per_total_total":pinbr_per_total_total,
        "16 pin_market_per_total_total":pin_market_per_total_total,
        "17 lwbr_val_total_total":lwbr_val_total_total,
        "18 lwbr_per_total_total":lwbr_per_total_total,
        "19 lw_market_per_total_total":lw_market_per_total_total,
        "20 lybr_val_total_total":lybr_val_total_total,
        "21 lybr_per_total_total":lybr_per_total_total,
        "22 ly_market_total_total":ly_market_total_total,
        "23 w_lift_req_total_total":w_lift_req_total_total,
        "24 brsls_total_total":brsls_total_total,
        "25 br_stk_total_total":br_stk_total_total,
        "26 br_space_total_total":br_space_total_total,
        "27 market_sls_total_total":market_sls_total_total,
        "28 market_stk_total_total":market_stk_total_total,
        "29 market_space_total_total":market_space_total_total,
        "30 act_ft_total_total":act_ft_total_total,
        "31 br_ft_total_total":br_ft_total_total,
        "32 market_ft_total_total":market_ft_total_total,
        "33 stok_actbr_u_total_total":stok_actbr_u_total_total,
        "34 stok_br_u_total_total":stok_br_u_total_total,
        "35 stok_actbr_cover_total_total":stok_actbr_cover_total_total,
        "36 stok_act_market_cover_total_total":stok_act_market_cover_total_total,
    }
    dictionary[zzz]=report_values_total_total
    return json.dumps(dictionary, sort_keys = True)

# b = '2016-07-03'
# c = '2016-07-09'
# a = bwt_report(b,c)
# x =0
# print(a)
