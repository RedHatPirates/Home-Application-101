from PySide2.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from login_pyside24 import Ui_MainWindow
from time import sleep
from threading import Timer
from card_db_fun import Chart_one
from datetime import datetime
from frame_bank.card_frame_bank import CardFrameBank
from source_ui.shadow import InitShadow ,set_shadow

import card_db_fun
import home_db_fun
import home_db_query
import pyautogui
import database
import webbrowser
import sys
import os
import database
import effects
import sys
import functions
import atexit
import requests


from home_db_fun import Loading_screen_gif
WINDOW_SIZE = 0
TOGLE_STATUS = 80
CARD_SELECTED = 0
GLOBAL_VERSION = '1.23'


class MainWindow(Ui_MainWindow,QtWidgets.QMainWindow):
     stackSignal = Signal()
     def __init__(self, parent=None):
         super(MainWindow, self).__init__(parent)
         self.setAttribute(Qt.WA_DeleteOnClose)
         self.setWindowFlags(Qt.FramelessWindowHint)
         self.setupUI(self)
         self.show()
         self.center()
         self.ui = Ui_MainWindow()
         global window_obj
         window_obj = self.ui

# SHADOWS FOR FRAME
         set_shadow.sets(self)
 

        
         #NOTIFICATION IF CLICKED ACTION
         tray.messageClicked.connect(lambda: messageClicked(self))
         action_hide.triggered.connect(lambda: self.hide())
         action_show.triggered.connect(lambda: self.showNormal())
        
         # SOURCE OF THE TABLE MENU
         self.font = QFont()
         self.font.setFamily(u"Bahnschrift Light Condensed")
         self.font.setPointSize(14)
        
         # CONFIGURING THE TABLE
         self.table = self.tableWidget
         self.table.verticalHeader().setVisible(False)
         self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
         self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
         self.table.verticalHeader().setDefaultSectionSize(50)
         self.table.setFont(self.font)
         self.table.horizontalHeaderItem(0).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
         self.table.horizontalHeaderItem(2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
         self.table.setStyleSheet("QWidget { color: #fffff8; border-radius:0px; } QHeaderView::section { background-color: rgb(53, 53, 53); border:none; width:45px; height: 50px ; border-radius:0px; } QTableWidget { gridline-color: #fffff8; border-radius:0px; border-radius:0px; } QTableWidget QTableCornerButton::section { background-color: #646464; border-radius:0px; } QTableView:item { border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0)); border-radius:0px; } QTableView::item:selected{ background-color:rgba(255, 255, 255,30); color: rgb(255, 255, 255); }")
         self.extrato_cartao_0.setStyleSheet("QWidget { color: #fffff8; border-radius:0px; } QHeaderView::section { background-color: rgb(53, 53, 53); border:none; width:45px; height: 50px ; border-radius:0px; } QTableWidget { gridline-color: #fffff8; border-radius:0px; border-radius:0px; } QTableWidget QTableCornerButton::section { background-color: #646464; border-radius:0px; } QTableView:item { border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0)); border-radius:0px; } QTableView::item:selected{ background-color:rgba(255, 255, 255,30); color: rgb(255, 255, 255); }")
         self.table_invoices_ind.setStyleSheet("QWidget { color: #fffff8; border-radius:0px; } QHeaderView::section { background-color: rgb(53, 53, 53); border:none; width:45px; height: 50px ; border-radius:0px; } QTableWidget { gridline-color: #fffff8; border-radius:0px; border-radius:0px; } QTableWidget QTableCornerButton::section { background-color: #646464; border-radius:0px; } QTableView:item { border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0)); border-radius:0px; } QTableView::item:selected{ background-color:rgba(255, 255, 255,30); color: rgb(255, 255, 255); }")
         self.table.horizontalHeader().sectionClicked.connect(self.filter_table_header)
        
         #StlypeSheet vertical ScrollBar
        
         #HIDDEN TABLE
         self.table.setColumnHidden(1, True)
         self.table.setColumnHidden(2, True)
         self.table.setColumnHidden(11, True)
        
         self.table.setColumnHidden(4, True)
         # COLUMN SIZE
         #CHECK
         self.table.setColumnWidth(0, 25)
         # ICON COLUMN
         self.table.setColumnWidth(3, 60)
         # DATE COLUMN
         self.table.setColumnWidth(5, 100)
         # PRIORITY COLUMN
         self.table.setColumnWidth(6, 150)
         # CATEGORY COLUMN
         self.table.setColumnWidth(7, 170)
         # PAYMENT COLUMN:
         self.table.setColumnWidth(8, 150)
         # COLUMN VALUE
         self.table.setColumnWidth(9, 300)
         # SATUS COLUMN
         self.table.setColumnWidth(10, 80)
         # COLUMN CATEGORY CARD TABLE
         self.card_extract_0.setColumnWidth(1, 150)


#CONFIGURING ACCOUNT IF YOU HAVE A CREDIT CARD
         self.comboBox_24.currentIndexChanged.connect(lambda:home_db_fun.mainpage._event_change_stakecard(self))
         self.comboBox_25.currentIndexChanged.connect(lambda:home_db_fun.mainpage._categorias_entra_said(self))
         self.comboBox_22.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_programar_date(self))
         self.comboBox_23.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_recorrencia_options(self))
         self.comboBox_23.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_recorrencia_options(self))
         self.comboBox_26.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_set_day_recurrence(self))
        
         #PDFVIEWER:
         self.listWidget_2.itemDoubleClicked.connect(lambda:home_db_fun.mainpage.open_pdf(self))
         #HIDE THE COLUMNS AND BUTTONS TABLE MENU
        
        
         self.frame_if_card_main.hide()
         self.label_if_card.hide()
         self.frame_options_pdf.hide()

        
        
         self.save_4.clicked.connect(lambda:self.close())
         self.exit.clicked.connect(lambda: self.close())
         self.minimize.clicked.connect(lambda: self.showMinimized())
         self.maxmize.clicked.connect(lambda: self.restore_or_maximize_window())
         self.pushButton_7.clicked.connect(lambda:self.pop_error.hide())
         self.pop_error.hide()
         self.pop_error_card.hide()
        
         self.buton_login.clicked.connect(self.check_field)
         self.pushButton.clicked.connect(self.toggleMenu)
         self.save_6.clicked.connect(lambda:database.save_data.testedb(self))
         self.save_5.clicked.connect(self.logout)

         # print(self.comboBox_2.count()-1)
         # print(self.comboBox_2.itemText(1))
        

         self.nova_despesa.clicked.connect(lambda:self.stacked_configcard0.setCurrentWidget(self.page_new_lancamento))
         effects.Effetc_slides.menu_card(self)
        
         #HIDE COLUMN CARD EXTRACT ID
         self.card_extract_0.setColumnHidden(7, True) # COLUMN ID HIDDEN
         self.extrato_cartao_0.setColumnHidden(8, True) # SUM DATE FOR HIDDEN FILTER
         self.extrato_cartao_0.setColumnHidden(9, True) # PAYMENT STATUS FOR FILTER HIDDEN
         self.table_invoices_ind_3.setColumnHidden(3, True) # COLUMN ID HIDDEN
         self.table_active_cards.setColumnHidden(6, True) # COLUMN ID HIDDEN

#HIDDEN ACTIVE BANKS TABLE
        
         self.table_active_banks.setColumnHidden(0, True) # COLUMN ID HIDDEN
         self.table_active_banks.setColumnHidden(1, True) # INITIAL BALANCE COLUMN
         self.table_active_banks.setColumnHidden(6, True) # COLUMN ID CREDIT CARD
        
         # entire line selection
         self.table_active_banks.setSelectionBehavior(QAbstractItemView.SelectRows)
        
         self.table_invoices_ind_3.horizontalHeader().setVisible(True)
         self.table_invoices_ind.horizontalHeader().setVisible(True)
         self.table_active_cards.horizontalHeader().setVisible(True)
         self.table_active_banks.horizontalHeader().setVisible(True)
         self.table_invoices_ind_3.horizontalHeader().setDefaultSectionSize(310)
         self.table_active_cards.horizontalHeader().setDefaultSectionSize(145)
         self.table.horizontalHeader().setVisible(True)
        
        
        
        
         self.extract_months.setTransitionDirection(QtCore.Qt.Horizontal)
         self.extract_months.setTransitionSpeed(500)
         self.extrat_meses.setTransitionEasingCurve(QtCore.QEasingCurve.InOutExpo)
         self.extract_months.setSlideTransition(True)
        
         self.grid.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page))
         self.grid_2.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page2))
         effects.Effetc_slides.grid_cards(self)
         effects.Effetc_slides._conent_geral_cards(self)
        
         self.add_card_3.clicked.connect(lambda:card_db_fun.card_functions.add_card(self))
         self.apaga_compra.clicked.connect(lambda:card_db_fun.cartao_funcoes.remove_compra(self))
         self.pushButton_6.clicked.connect(self.open_webbrowser)
         self.pushButton_17.clicked.connect(lambda:card_db_fun.card_functions.today(self))
       
         # TIMERS
        
         # self.timer.timeout.connect(card_db_fun.card_functions._clock_page_cards(self))
         self.timer = QTimer(self)
         self.timer.timeout.connect(lambda:card_db_fun.cartao_funcoes._clock_page_cards(self))
         self.timer.start(1000)

#RADIO CONFIG:
         self.hidden_balance_fat0_true.clicked.connect(lambda:home_db_fun.Configs.hide_show_balance_zeros(self,True))
         self.hidden_saldo_fat0_false.clicked.connect(lambda:home_db_fun.Configs.hide_show_balance_zeros(self,False))
        
         #SHADOW ENABLE OR DISABLE
         self.shadow_true.clicked.connect(lambda:home_db_fun.Configs.show_hide_shadow(self,True))
         self.shadow_false.clicked.connect(lambda:home_db_fun.Configs.show_hide_shadow(self,False))
        
        
         self.hide_cards_main_2.clicked.connect(lambda:home_db_fun.Confirn_Frame._show(self))
        
        
         # self.show_cards_main_2.clicked.connect(lambda:home_db_fun.Loading_screen_gif.close_loading(self))
        
        
         card_db_fun.Main_page_Cards._itemlist_metas(self)
         # EVENT FILTER #
        
         self.pushButton_8.installEventFilter(self)
         self.pushButton_9.installEventFilter(self)
         self.pushButton_10.installEventFilter(self)
         self.pushButton_11.installEventFilter(self)
         self.pushButton_12.installEventFilter(self)
         self.pushButton_14.installEventFilter(self)
         self.pushButton_15.installEventFilter(self)
         self.pushButton_16.installEventFilter(self)
         self.pushButton_18.installEventFilter(self)
         self.previus_month.installEventFilter(self)
         self.next_month.installEventFilter(self)
         self.filter_dates_btn.installEventFilter(self)
         self.pushButton_3.installEventFilter(self)
         self.pushButton_2.installEventFilter(self)
         self.compras.installEventFilter(self)
         self.invoices.installEventFilter(self)
         self.paga_invoice.installEventFilter(self)
         self.lanca.installEventFilter(self)
         self.next_month_3.installEventFilter(self)
         self.previus_month_3.installEventFilter(self)
         self.pushButton_14.installEventFilter(self)
         self.back_main_dash.installEventFilter(self)
         self.pushButton_20.installEventFilter(self)
         self.hide_cards_main.installEventFilter(self)
         self.show_cards_main.installEventFilter(self)
         self.hide_cards_det.installEventFilter(self)
         self.show_cards_det.installEventFilter(self)
         self.table_invoices_ind_3.installEventFilter(self)
         self.listWidget.installEventFilter(self)
         self.table_active_cards.installEventFilter(self)
         self.pushButton_23.installEventFilter(self)
         self.table.installEventFilter(self)
         self.add_bank.installEventFilter(self)
         self.add_lancamento_btn.installEventFilter(self)
         self.previus_month_2.installEventFilter(self)
         self.next_month_2.installEventFilter(self)
         self.paga_fatura_3.installEventFilter(self)
         self.download_pdf_2.installEventFilter(self)
         self.download_pdf.installEventFilter(self)
         self.toolButton_pdf_opt.installEventFilter(self)
         self.config_ccoun.installEventFilter(self)
         self.config_crdit_c.installEventFilter(self)
         self.parcela_fatura_3.installEventFilter(self)
         self.paga_fatura_4.installEventFilter(self)
         self.listWidget_3.installEventFilter(self)
         self.table_active_banks.installEventFilter(self)
         self.update_bank.installEventFilter(self)
         self.remove_bank.installEventFilter(self)
         self.apaga_compra_3.installEventFilter(self)
         self.btn_if_card_2.installEventFilter(self)
         self.remove_card_3.installEventFilter(self)
         self.frame_43.installEventFilter(self)
         self.show_cards_main_2.installEventFilter(self)
         self.hide_cards_main_3.installEventFilter(self)
         self.next_month_4.installEventFilter(self)
         self.previus_month_4.installEventFilter(self)
         #EVENTS APP
         self.bar_window.installEventFilter(self)

# MODEL WORKSHEETS
         self.pushButton_29.installEventFilter(self)
         self.pushButton_30.installEventFilter(self)
         self.create_xlsx_file.installEventFilter(self)

        
    
     def eventFilter(self, obj, event):
        
             #EVENTS APP
             if obj == self.bar_window and event.type() == QtCore.QEvent.MouseButtonDblClick:
                 if self.isMaximized():
                     self.showNormal()
                 else:
                     self.showMaximized()
             #MOUSE HOVER EVENT
             if obj == self.frame_43 and event.type() == QtCore.QEvent.Enter:
                 event = 'enter'
                 return effects.Hover_Event_Frames._btns_top_main(self,event)
            
             if obj == self.frame_43 and event.type() == QtCore.QEvent.Leave:
                 event = 'leave'
                 return effects.Hover_Event_Frames._btns_top_main(self,event)

             #EVENTS BUTTONS AND WIDGETS
             if obj == self.next_month_4 and event.type() == QtCore.QEvent.MouseButtonPress:
                 action = 'next'
                 return home_db_fun.Charts_Main.Update_Year_Filter(self,action)
            
             if obj == self.previus_month_4 and event.type() == QtCore.QEvent.MouseButtonPress:
                 action = 'previous'
                 return home_db_fun.Charts_Main.Update_Year_Filter(self,action)
            
             #btn dashboard main
             if obj == self.show_cards_main_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                 self.staked_bottom_main.setCurrentWidget(self.page_dashboard_btn_main)
                 self.extract_months_2.setCurrentWidget(self.page_12)
                 effects.Enable_Slide._slide(self,self.staked_bottom_main)
                 effects.Enable_Slide._slide(self,self.extract_months_2)
                 return home_db_fun.Charts_Main.Update_Chart_E_S_GERAL(self)
             #btn dashboard main switch back to main
             if obj == self.hide_cards_main_3 and event.type() == QtCore.QEvent.MouseButtonRelease:
                 self.extract_months_2.setCurrentWidget(self.page_11)
                 return self.staked_bottom_main.setCurrentWidget(self.main_dash_bottom_2Page1)

if obj == self.pushButton_8 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="account"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
             if obj == self.pushButton_9 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn = "investment"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
             if obj == self.pushButton_10 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="card"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
             if obj == self.pushButton_11 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="transfer"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
             if obj == self.pushButton_15 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="stock"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
            
             if obj == self.pushButton_16 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="config"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)

             if obj == self.previus_month and event.type() == QtCore.QEvent.MouseButtonPress:
                 action = "Previous"
                 objects = self.page_2
                 effects.Effetc_slides.grid_filter(self,action,objects)
                 card_db_fun.card_functions._current_date(self, action)
                 return card_db_fun.Chart_one.clear(self)

            
             if obj == self.next_month and event.type() == QtCore.QEvent.MouseButtonPress:
                 action = "Next"
                 objects = self.page_2
                 effects.Effetc_slides.grid_filter(self,action,objects)
                 card_db_fun.card_functions._current_date(self, action)
                 return card_db_fun.Chart_one.clear(self)
            
             if obj == self.pushButton_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                
                 #TODO VOLTA FILTER NEXT AND PREV MONTHS
                 self.extract_months.setCurrentWidget(self.page_2)
                 self.stack_extrato_pages.setCurrentWidget(self.extrato_cards_dbs)
                 month = card_db_fun.funcoes_cartao._mes2(self)
                 card_db_fun.cartao_funcoes._return_month_string(self)
                 card_db_fun.card_functions._current_date(self,'none')
                 return card_db_fun.funcoes_cartao.carga_extrato_month(self,month)

             if obj == self.pushButton_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                 #ALL FILTRA PURCHASE
                 return card_db_fun.funcoes_cartao._search_shopping(self)

             if obj == self.shopping and event.type() == QtCore.QEvent.MouseButtonPress:
                 # ALL PURCHASES RIGHT MENU
                 card_db_fun.cartao_funcoes._return_month_string(self)
                 card_db_fun.card_functions._current_date(self,"none")
                 self.extract_months.setCurrentWidget(self.page_2)
                 return self.stacked_configcard0.setCurrentWidget(self.page_extract)



             if obj == self.invoices and event.type() == QtCore.QEvent.MouseButtonPress:
                 # ALL PURCHASES RIGHT MENU
                 self.extract_months.setCurrentWidget(self.page_8)
                 return self.stacked_configcard0.setCurrentWidget(self.page_Invoices)
            

             if obj == self.next_month_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                 # ALL PURCHASES RIGHT MENU
                 objects = self.page_8

                 action = "Next"
                 effects.Effetc_slides.grid_filter(self,action,objects)
                 card_db_fun.card_functions._filter_year_invoices(self,"Next")
                 return card_db_fun.funcoes_cartao._invoices(self)
            


             if obj == self.previus_month_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                 # ALL PURCHASES RIGHT MENU
                 objects = self.page_8
                 action="Previous"
                 effects.Effetc_slides.grid_filter(self,action,objects)
                 card_db_fun.cartao_funcoes._filter_year_faturas(self,"Previus")
                 return card_db_fun.funcoes_cartao._invoices(self)
            
            
             if obj == self.paga_fatura and event.type() == QtCore.QEvent.MouseButtonPress:
                 # ALL PURCHASES RIGHT MENU
                 card_db_fun.funcoes_cartao._pagar_fatura(self)
                 card_db_fun.funcoes_cartao._invoices(self)
                 card_db_fun.card_functions._current_date(self,"none")
                 card_db_fun.Main_page_Cards._top_main_values_update(self)
                 card_db_fun.Main_page_Cards._middle_main_values_update(self)
                 return card_db_fun.funcoes_cartao._Values_Individual(self)

if obj == self.filter_dates_btn and event.type() == QtCore.QEvent.MouseButtonPress:
                 # ALL PURCHASES RIGHT MENU
                 self.extrat_months.setCurrentWidget(self.extrat_monthsPage1)
                 self.extrat_meses.setStyleSheet("border-radius:7px; background-color: rgba(0, 0, 0,0); ")
                 return 0

             if obj == self.pushButton_12 and event.type() == QtCore.QEvent.MouseButtonPress:
                 return self.stacked_configcard0.setCurrentWidget(self.options_top_xls)
            
            
             if obj == self.lanca and event.type() == QtCore.QEvent.MouseButtonPress:
                 card_db_fun.funcoes_cartao._addRow(self)
                 card_db_fun.funcoes_cartao._invoices(self)
                 return card_db_fun.card_functions._current_date(self,"none")
            
             if obj == self.pushButton_14 and event.type() == QtCore.QEvent.MouseButtonPress:
                 self.stacked_configcard0.setCurrentWidget(self.charts_individual)
                 self.extract_months.setCurrentWidget(self.page_2)
                 return Chart_one._creat_charts(self)
            
             if obj == self.pushButton_18 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="dev"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
            
             if obj == self.back_main_dash and event.type() == QtCore.QEvent.MouseButtonPress:
                
                 return self.card_details.setCurrentWidget(self.dashboard_cards)
                
            
             if obj == self.pushButton_20 and event.type() == QtCore.QEvent.MouseButtonPress:
                
                 return self.card_details.setCurrentWidget(self.card_detailsPage1)
            
            
             #all Animation cards grid
             if obj == self.hide_cards_main and event.type() == QtCore.QEvent.MouseButtonPress:
                 return effects.Effetc_slides._hide_group_cards(self)
             if obj == self.hide_cards_det and event.type() == QtCore.QEvent.MouseButtonPress:
                 return effects.Effetc_slides._hide_group_cards(self)

             if obj == self.table_faturas_ind_3 and event.type() == QtCore.Qt.LeftButton or event.type() == QtCore.Qt.RightButton:
                 try:
                     self.table_invoices_ind_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                     row = self.table_invoices_ind_3.currentRow()
                     id = self.table_invoices_ind_3.item(line,3).text()
                     card_db_fun.Main_page_Cards._table_main_values_update(self,id)
                 except: 
                          pass
             if obj == self.listWidget and event.type() == QtCore.Qt.LeftButton or event.type() == QtCore.Qt.RightButton:
                 try:
                     currentcate = self.listWidget.currentItem().text()
                     card_db_fun.Main_page_Cards._categoria_metas(self,currentcate)
                 except:
                     pass

             if obj == self.table_active_cards and event.type() == QtWidgets.QAbstractItemView.SelectRows:
                 try:
                     self.table_active_cards.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                     row = self.table_active_cards.currentRow()
                     id = self.table_active_cards.item(line,6).text()
                     card_db_fun.funcoes_cartao.style_config_card_talbe_slected(self,id)
                    
                 except:
                     pass
                
             if obj == self.pushButton_23 and event.type() == QtCore.QEvent.MouseButtonPress:
                 try:
                     card_db_fun.funcoes_cartao._update_cards_config(self)
                     card_db_fun.funcoes_cartao._update_table_config(self)
                 except:
                     pass

             if obj == self.table and event.type() == QtWidgets.QAbstractItemView.SelectRows:
                 current_row = self.table.currentRow()
                 current_column = self.table.currentColumn()
                 try:
                     id = self.table.item(current_row, 1).text()
                     type = home_db_fun.Descricao_lancamento._verifi_is_credit_card(self,id)
    
                     #PRINT CELL WIDGET TEXT
                    
    
                     id = self.table.item(current_row, 1).text()
                     id_bank = self.table.item(current_row, 2).text()
                     #IF ENTRY, CHANGE PAYMENT BUTTON TEXT
                     home_db_fun.Description_lancamento.Change_text_btn_pagar_receber(self,id)
                     #CALL QUERY TO GET THE RELEASE DESCRIPTION
                     validator = home_db_fun.Lance_Description.set_lancamento_description(self,id)
                     #SET TEXT RELEASE DETAILS:
                    
                    
                     self.frame_options_pdf.hide()
                     if validator=="invoice":
                         home_db_fun.Description_lancamento.set_icon_desc(self,id)
                     else:
                         self.frame_if_card_main.hide()
                         self.label_if_card.hide()
                    
                     home_db_fun.Pdf_funtion.search_pdf(self,id,id_bank)
                    
                     if type == True:
                         home_db_fun.Description_lancamento.set_details_lancamneto_menu(self,id,id_bank,"invoice")
                     else:
                         home_db_fun.Description_lancamento.set_details_lancamneto_menu(self,id,id_bank,"lancamento")
                 except:
                     pass



             if obj == self.add_bank and event.type() == QtCore.QEvent.MouseButtonPress:
                
                 return home_db_fun.mainpage._add_bank(self)

             if obj ==self.add_lancamento_btn and event.type() == QtCore.QEvent.MouseButtonPress:
                
                 return home_db_fun.mainpage._new_lancamento(self)

# ALL EXTRACT MAIN MENU
            
            
             if obj == self.previus_month_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                 action="Previous"
                 home_db_fun.Dates_end_times.methodo_date_extrato(self,action)
                 home_db_fun.mainpage.load_extrato_filter(self)
                 return home_db_fun.Charts_Main.Update_Chart_E_S(self)
                
             if obj == self.next_month_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                 action="Next"
                 home_db_fun.Dates_end_times.methodo_date_extrato(self,action)
                 home_db_fun.mainpage.load_extrato_filter(self)
                 return home_db_fun.Charts_Main.Update_Chart_E_S(self)

             if obj == self.paga_fatura_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                 current_row = self.table.currentRow()

                 if self.paga_fatura_3.text() == "Pay":
                    
                     return home_db_fun.Pagamento._pagar_lancamento(self)
                 elif self.paga_fatura_3.text() == "Pay Invoice":
                     return home_db_fun.Payment._pagar_invoice(self)
                 else:
                     return home_db_fun.Pagamento._receber_lancamento(self)
                 
             if obj == self.download_pdf_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                     #SELECT PDF TO SAVE AT LAUNCH
                 return home_db_fun.Pdf_funtion.open_pdf(self)
            
            
             if obj == self.download_pdf and event.type() == QtCore.QEvent.MouseButtonPress:
                 return home_db_fun.Pdf_funtion.save_pdf(self)
            
            
             if obj == self.toolButton_pdf_opt and event.type() == QtCore.QEvent.MouseButtonPress:
                 return home_db_fun.Pdf_funtion.options_tool_btn_file(self)
            
             if obj == self.config_ccoun and event.type() == QtCore.QEvent.MouseButtonPress:
                 effects.Effetc_slides._add_banks_credits(self)
                 return self.stackedWidgetadc_2.setCurrentWidget(self.page_config_counts1)
            
             if obj == self.config_crdit_c and event.type() == QtCore.QEvent.MouseButtonPress:
                 effects.Effetc_slides._add_banks_credits(self)
                 return self.stackedWidgetadc_2.setCurrentWidget(self.page_config_creduts)
            
             #LAUNCH DETAILS:
             if obj == self.parcela_fatura_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                 effects.Effetc_slides._detail_launch_slide(self)
                 return self.stackedWidget_58.setCurrentWidget(self.stackedWidget_launch_details)
            
             #VOLTA MENU DETAILS LAUNCH I:
             if obj == self.paga_fatura_4 and event.type() == QtCore.QEvent.MouseButtonPress:
                 effects.Effetc_slides._detail_launch_slide(self)
                 return self.stackedWidget_58.setCurrentWidget(self.stackedWidget_summary_extract)
            
             # PRESSING DELETE DELETES THE SELECTED ITEM FROM THE PDFS FOR RELEASES
             if obj == self.listWidget_3 and event.type() == QtCore.QEvent.KeyPress:
                 if event.key() == QtCore.Qt.Key_Delete:
                     return self.listWidget_3.takeItem(self.listWidget_3.currentRow())

             if obj == self.table_active_banks and event.type() == QtWidgets.QAbstractItemView.SelectRows:
                 current_row = self.table_active_banks.currentRow()
                
                 id_bank = self.table_active_banks.item(current_row, 0).text()
                 id_card = self.table_active_banks.item(current_row, 6).text()
                 home_db_fun.Table_Banks_Remove_Update.set_values_frame(self,id_bank,id_card)
                 return print(id_bank, id_card)
             if obj == self.update_bank and event.type() == QtCore.QEvent.MouseButtonPress:
                 current_row = self.table_active_banks.currentRow()
                 id_bank = self.table_active_banks.item(current_row, 0).text()
                 id_card = self.table_active_banks.item(current_row, 6).text()
                    
                    
                 return home_db_fun.Table_Banks_Remove_Update._update_table_banks(self,id_bank,id_card)
            
             if obj == self.remover_bank and event.type() == QtCore.QEvent.MouseButtonPress:
                 current_row = self.table_active_banks.currentRow()
                 id_bank = self.table_active_banks.item(current_row, 0).text()
                 id_card = self.table_active_banks.item(current_row, 6).text()
                    
                    
                 return home_db_fun.Table_Banks_Remove_Update._remove_table_banks(self,id_bank,id_card)
            
             if obj == self.apaga_compra_3 and event.type() == QtCore.QEvent.MouseButtonPress: #TODO APAGA LANCAMENTO
                 current_row = self.table.currentRow()

                 id = self.table.item(current_row, 1).text()
                 id_bank = self.table.item(current_row, 2).text()
                 return home_db_fun.Remove_lancamentos._Delet_lancamento(self,id)
            
             if obj == self.btn_if_card_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                 btn="card"
                 return effects.Effetc_slides.grid_lateral_menu(self,btn)
            
             if obj == self.remover_card_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                 current_row = self.table_active_cards.currentRow()
                 id_bank = self.table_active_cards.item(current_row, 6).text()
                 # check if there is a linked database
                 return card_db_fun.funcoes_cartao.delete_card_if_bank_v(self,id_bank)
# module worksheets
             if obj == self.pushButton_29 and event.type() == QtCore.QEvent.MouseButtonPress:
                 return home_db_fun.Sheets_Main.Open_and_Read(self)
            
             if obj == self.pushButton_30 and event.type() == QtCore.QEvent.MouseButtonPress:
                 return card_db_fun.funcoes_cartao._add_New_Lancamento_xlsx(self)
            
             if obj ==self.create_xlsx_file and event.type() == QtCore.QEvent.MouseButtonPress:
                 return home_db_fun.Sheets_Main.Cria_Model_Xlsx(self)
            
             return super(MainWindow,self).eventFilter(obj, event)
        
        


     def check_field(self):

         user = ""
         password = ""

         def Appear_message(message):
             self.pop_error.show()
             self.text_error.setText(message)

         #EVERY CZECH USER STILL CONNECT WITH DB
         if not self.enter_user.text():
             username = "User not found"
         else:
             user = ""
         #ALL CHECK PASSWORD
         if not self.enter_pass.text():
             password = "Password not found"
         else:
             password = ""
         # check user

         if username + password != '':
             text = username + password
             Appear_message(text)

         else:
            
             text = "Welcome"
             Appear_message(text)

             self.shows()
             a = (os.path.dirname(os.path.realpath(__file__)))
             if (os.path.exists(''+a+'/bando_de_valores.db')):
                 card_db_fun.card_functions.hide_show_logoff(self)
                 card_db_fun.funcoes_cartao._start_values(self)
                 title ='Updates'
                 message = 'Checking for Update'
                 try:
                     card_db_fun.funcoes_cartao.group_main(self)
                    
                 except:
                     pass
                 # home_db_fun.Set_values_startup.set_values_table_bank(self)
                 home_db_fun.Group.execs(self)
                 home_db_fun.Charts_Main._Active_sharts(self)
                
                 self.update()
                 show_tray_message(self.ui, tray, title, message)
             else:
                 self.CONTAINER_general.hide()
                 pyautogui.confirm(text='!!ATTENTION!!\nDatabase not found, Please Create file in MENU>CREATE DATABASE',title='DATABASE NOT LOCATED', buttons=['OK', 'Cancel'])
                 database.save_data.testedb(self)
                
             self.select_card.currentTextChanged.connect(lambda:card_db_fun.card_functions.style_config_card(self))
             self.comboBox_2.currentTextChanged.connect(lambda:card_db_fun.cartao_funcoes.changeexpenses(self))
             self.lineEdit_3.textChanged.connect(lambda:card_db_fun.cartao_funcoes.raname_value(self))
             self.lineEdit_2.textChanged.connect(lambda:card_db_fun.cartao_funcoes.raname_date(self))
             functions.general_functions.date_time(self)
            



         if self.checkBox.isChecked():
             text = text + "User Saved"
             Appear_message(text)

     #TODO AFTER CHECK LOGIN, OPEN THE MAIN:
     def shows(self):
         self.stackedWidget.setCurrentIndex(1)
         self.stacked_configcard0.setCurrentIndex(0)
        
     #ALL IF YOU CLICK LOGOUT
     def logout(self):
         self.stackedWidget.setCurrentIndex(0)
         self.text_error.setText("System Off, See You!")



     def filter_table_header(self, logicalIndex):
         #TEMPORARY ROLE HERE DPS FOR HOME DB FUN
         icon4 = QIcon()
        
         if logicalIndex >1:
        
             if self.table.horizontalHeaderItem(logicalIndex).data(256) == "DOW":
                 item = self.table.horizontalHeaderItem(logicalIndex)
                 icon4.addFile(u":/main_menutable/main_page_tables/decrecente.png", QSize(), QIcon.Normal, QIcon.Off)
                 self.table.horizontalHeaderItem(logicalIndex).setData(256, "UP")
                 item.setIcon(icon4)

             else:
                 item = self.table.horizontalHeaderItem(logicalIndex)
                 icon4.addFile(u":/main_menutable/main_page_tables/ascendente.png", QSize(), QIcon.Normal, QIcon.Off)
                 self.table.horizontalHeaderItem(logicalIndex).setData(256, "DOW")
                 item.setIcon(icon4)
         else:
            
             if self.table.cellWidget(0, 0).isChecked() ==False:
                 row_count = self.table.rowCount()
                 item = self.table.horizontalHeaderItem(logicalIndex)
                 icon4.addFile(u":/main_menutable/main_page_tables/checked.png", QSize(), QIcon.Normal, QIcon.Off)
                 item.setIcon(icon4)
                 for i in range(row_count):
                     self.table.cellWidget(i, 0).setChecked(True)
             else:
                 row_count = self.table.rowCount()
                 item = self.table.horizontalHeaderItem(logicalIndex)
                 icon4.addFile(u":/main_menutable/main_page_tables/unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
                 item.setIcon(icon4)
                 for i in range(row_count):
                     self.table.cellWidget(i, 0).setChecked(False)
         return true
def center(self):
         qr = self.frameGeometry()
         cp = QDesktopWidget().availableGeometry().center()
         qr.moveCenter(cp)
         self.move(qr.topLeft())
     # ALL TEST ANIMATION EXPANDED MENU
     def toggleMenu(self):
         global TOGLE_STATUS
         STATUS = TOGLE_STATUS
         duration = 500
         if STATUS == 80:
                
                 # ALL ANIMATION EXPANDING
                 self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
                 self.animation.setDuration(duration)
                 self.animation.setStartValue(80)
                 self.animation.setEndValue(250)
                 self.animation.setEasingCurve(QEasingCurve.OutExpo)
                 self.animation.start()
                
                 TOGLE_STATUS = 150


         else: #ALL ANIMATION RETRACTING maximumHeight
                 self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
                 self.animation.setDuration(duration)
                 self.animation.setStartValue(250)
                 self.animation.setEndValue(80)
                 self.animation.setEasingCurve(QEasingCurve.OutExpo)
                 self.animation.start()
                 TOGLE_STATUS = 80

     def card(self):
         global CARD_SELECTED
         return CARD_SELECTED

     def restore_or_maximize_window(self):
         # global variable windows screen window
         global WINDOW_SIZE
         win_status = WINDOW_SIZE
         if win_status == 0:
             WINDOW_SIZE = 1
             self.showFullScreen()
             # self.extract_card_0.horizontalHeader().setDefaultSectionSize(120)
             # self.card_extract_0.verticalHeader().setDefaultSectionSize(40)
             # font8 = QFont()
             # font8.setFamily(u"Microsoft YaHei")
             # font8.setPointSize(12)
             # self.extrato_cartao_0.setFont(font8)
             # self.card_extract_0.setIconSize(QSize(40, 40))
             # self.table_invoices_ind.horizontalHeader().setDefaultSectionSize(255)
             # self.card_extract_0.setColumnWidth(1, 150)

         else:
             WINDOW_SIZE = 0
             self.showNormal()
             # font8 = QFont()
             # font8.setFamily(u"Microsoft YaHei")
             # font8.setPointSize(10)
             # self.extrato_cartao_0.setFont(font8)
             # self.card_extract_0.setIconSize(QSize(35, 35))
             # self.extract_card_0.horizontalHeader().setDefaultSectionSize(100)
             # self.card_extract_0.verticalHeader().setDefaultSectionSize(40)
             # self.table_invoices_ind.horizontalHeader().setDefaultSectionSize(189)
             # self.card_extract_0.setColumnWidth(1, 150)

     def mousePressEvent(self, event):
         self.offset = event.pos()

     #MOVE WINDOW
     def mouseMoveEvent(self, event):
         try:
             if WINDOW_SIZE == 0:
                 x=event.globalX()
                 y=event.globalY()
                 if self.offset.y() <25:
                     x_w = self.offset.x()
                     y_w = self.offset.y()
                     self.move(x-x_w, y-y_w)
         except:
             pass
    
     def update(self):
         response = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
         with open ('version.txt','wb') as new_file:
             new_file.write(response.content)
        

         read = open('version.txt','r')
         access = read.readlines()
         split = str(access[0])
         version = split.split()[1]
         # access[0] = version
         # access[1 = notes]
         global GLOBAL_VERSION
         act_ver = GLOBAL_VERSION
         if version== act_ver:
             title = 'Important'
             message = 'No new version found'
             show_tray_message(window_obj, tray, title, message)
         else:
            
             title = 'Important'
             message = 'New version found click for details'
             show_tray_message(window_obj, tray, title, message)

     def open_webbrowser(self):
         webbrowser.open('https://github.com/xjhowxjhow')
################################################### ######################
def messageClicked(self):
     response = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
     with open ('version.txt','wb') as new_file:
         new_file.write(response.content)
        
     read = open('version.txt','r')
     access = read.readlines()
     split = str(access[0])
     version = split.split()[1]
     global GLOBAL_VERSION
     act_ver = GLOBAL_VERSION
     if version== act_ver:
         pass
     else:
         show_message()
################################################### ######################
# IT WILL ONLY APPEAR IF IT HAS UPDATE
################################################### ######################
def show_message():
     response = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
     with open ('version.txt','wb') as new_file:
         new_file.write(response.content)
        
     read = open('version.txt','r')
     access = read.readlines()
     split = str(access[1])
     try:
         response = requests.get('https://github.com/xjhowxjhow/HomeAplication1.0/blob/main/version/main.exe?raw=true')
         with open('HomeAppold.exe','wb') as new_file:
             new_file.write(response.content)
            
             msg = QMessageBox()
             msg.setIcon(QMessageBox.Information)
             msg.setWindowIcon(QtGui.QIcon(u":/menu/pngwing.com.png)"))
        
             msg.setWindowTitle("Update")
             msg.setText("New application update found, Click exit icon on taskbar to Exit application And Apply new version")
             msg.setInformativeText("Click hide to see what changed")
             msg.setDetailedText(split)
             msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
             msg.exec_()
             button = msg.clickedButton()
             sb = msg.standardButton(button)
             if sb == QMessageBox.Yes:
                 exit()
     except:
         QMessageBox.information(None,
                             "Error",
                             "Failed to update, please restart the application")
################################################### ######################
# Show tray message when action_tray_message tray action is clicked
################################################### ######################
def show_tray_message(self, tray: QSystemTrayIcon,title,message):
     print("show_tray_message")
     notificationTitle = title
     notificationMessage = message
     icon = QIcon(u":/icons-cards/src-page-cartoes/urgencia.png")
     duration = 10 * 1000 #3 seconds

     if len(notificationTitle) == 0 or len(notificationMessage) == 0:
         tray.showMessage("Input Something", "Enter your notification title and message", icon, duration)
     else:
         tray.showMessage(notificationTitle, notificationMessage, icon, duration)





def exit_handler():
     response = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
     with open ('version.txt','wb') as new_file:
         new_file.write(response.content)
        
     read = open('version.txt','r')
     access = read.readlines()
     split = str(access[0])
     version = split.split()[1]
     global GLOBAL_VERSION
     act_ver = GLOBAL_VERSION
     if version== act_ver:
         pass
     else:
    
         a = (os.path.dirname(os.path.realpath(__file__)))
         if(os.path.exists(''+a+'/update/update.exe')):
             os.startfile(''+a+'/update/update.exe')
             print("yes")
         sys.exit()
    



            
atexit.register(exit_handler)


if __name__ == '__main__':
     # os.environ["QT_FONT_DPI"] = "96"
     app = QtWidgets.QApplication(sys.argv)
     if not QSystemTrayIcon.isSystemTrayAvailable():
         QMessageBox.critical(None, "System Tray", "System tray was not detected!")
         sys.exit(1)
app.setQuitOnLastWindowClosed(True)
     tray = QSystemTrayIcon(QIcon(u":/menu/pngwing.com.png"), app)
     menu = QMenu()
     action_hide = QAction("Minimize Window")
     menu.addAction(action_hide)

     action_show = QAction("Show Window")
     menu.addAction(action_show)

     action_exit = QAction("Exit")
     action_exit.triggered.connect(app.exit)
     menu.addAction(action_exit)

     tray.setToolTip("HomeApplication")

     tray.setContextMenu(menu)

     tray.show()
     mainWin = MainWindow()
     ret = app.exec_()
     sys.exit()

