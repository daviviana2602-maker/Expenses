from sqlalchemy import create_engine, Column, Integer, String, Float, Date    # import used types
from sqlalchemy.orm import declarative_base, sessionmaker

import os   #clear screen

from utils import fanymodules as fm    # my own "lib"

from datetime import datetime    # import day and hour

from tabulate import tabulate   # print a beautiful table

from colorama import init, Back, Style    # colors
init()

from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)   # connect with the database
Session = sessionmaker(bind=engine)
Base = declarative_base()



#------------------- MENU -------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    #clear screen


def menu_choice():
    clear_screen()
    print(f'{Back.MAGENTA}============= M E N U ============={Style.RESET_ALL}')
    print('0 - Encerrar programa')
    print('1 - Registrar gasto')
    print('2 - Relatório por período')
    print('3 - Verificar tabela de gastos por período')


    choice = fm.input_choice(
            msg = 'Escolha uma opção do menu: ',
            valid_options = (0, 1, 2, 3),
            error_msg = 'Invalid option.',
            use_color = True
            )
    
    return choice



#------------------- CLASSES -------------------



class ExpensesTable(Base):   # class is mandatory with database
    __tablename__ = 'expenses'   # creating table expenses
    id = Column(Integer, primary_key=True)
    desc = Column(String)
    categoria = Column(String)
    valor = Column(Float)
    data = Column(Date)
    
    
Base.metadata.create_all(engine) # create all tables in database


#------------------- FUNÇÕES -------------------


def option_1():  # register cost
    while True:
        
            desc = fm.input_alpha(
                    msg = 'digite com o que foi gasto: ',
                    error_msg = 'digite um gasto válido.',
                    case = 'title',
                    use_color = True
                )


        
            category = fm.input_choice(
                msg = 'Qual foi o tipo do gasto (1) Residencial ou (2) Variável: ',
                valid_options = (1, 2),
                error_msg = 'Opção inválida.',
                use_color = True
            )
                    
            if category == 1:
                category = 'RESIDENCIAL'
                
            else:
                category = 'VARIÁVEL'
                


            value = fm.input_float(
                                msg = f'Digite o valor total gasto com {desc}: ',
                                min_value = None,
                                max_value = None,
                                error_msg = 'Valor inválido',
                                use_color = True
                            )
                
                
            date =  fm.input_date(
                                msg = 'Insira a data do gasto: ',
                                error_msg = 'Data inválida. Use o formato DD/MM/YYYY',
                                use_color = True
                            )


            with Session() as session:  #create session
            
            
                try:
                    new_record = ExpensesTable(desc = desc, categoria = category,
                                            valor = value, data = date)
                        
                    session.add(new_record)
                    session.commit()     # enter in PostgreSQL
                    print(f'{Back.GREEN}Gasto registrado com sucesso!{Style.RESET_ALL}')
                    
                except Exception as error:
                    session.rollback()
                    print(f'{Back.RED}ERRO: {error}{Style.RESET_ALL}')
            
            
            
            if not fm.get_confirm(
                            msg = 'deseja inserir outro gasto? (sim/não): ',
                            yes = 'sim',
                            no = 'não',
                            error_msg = 'opção inválida.',
                            use_color = True):   # verify if the program will repeat or no
                break
                    
                    
                    
def option_2():  # results
    while True:
        
        start_date, end_date = fm.input_date_range(
                                            start_msg = 'insira a data inicial (DD/MM/YYYY): ',
                                            end_msg = 'Insira a data final (DD/MM/YYYY): ',
                                            format_error_msg = 'Data inválida. Use DD/MM/YYYY.',
                                            range_error_msg = 'Data final deve vir após a data inicial.',
                                            use_color = True
                                        )


        with Session() as session:  # create session
        
        
            # taking expenses in the period
            expenses = session.query(ExpensesTable).filter(
                ExpensesTable.data >= start_date,
                ExpensesTable.data <= end_date
            ).all()
            
            
            # taking expenses in the period
            residencial_expenses = session.query(ExpensesTable).filter(
                ExpensesTable.data >= start_date,
                ExpensesTable.data <= end_date,
                ExpensesTable.categoria == 'RESIDENCIAL'
            ).all()
            
            
             # taking expenses in the period
            variable_expenses = session.query(ExpensesTable).filter(
                ExpensesTable.data >= start_date,
                ExpensesTable.data <= end_date,
                ExpensesTable.categoria == 'VARIÁVEL'
            ).all()
            
            
            if not expenses:
                print(f'{Back.RED}Não há gastos nesse período.{Style.RESET_ALL}')

            else:

                # calculate total expense
                total_expense = 0

                for e in expenses:
                    total_expense = total_expense + e.valor


                # calculate residential expense
                total_residencial = 0

                for e in residencial_expenses:
                    total_residencial = total_residencial + e.valor


                # calculate variable expense
                total_variable = 0

                for e in variable_expenses:
                    total_variable = total_variable + e.valor


                print(f'{Back.CYAN}Total gasto nesse período: R${total_expense:.2f}{Style.RESET_ALL}')
                print(f'{Back.CYAN}Total residencial gasto nesse período: R${total_residencial:.2f}{Style.RESET_ALL}')
                print(f'{Back.CYAN}Total variável gasto nesse período: R${total_variable:.2f}{Style.RESET_ALL}')
                break
                    


def option_3():   # table
    while True:
        
        start_date, end_date = fm.input_date_range(
                                                start_msg = 'insira a data inicial (DD/MM/YYYY): ',
                                                end_msg = 'Insira a data final (DD/MM/YYYY): ',
                                                format_error_msg = 'Data inválida. Use DD/MM/YYYY.',
                                                range_error_msg = 'Data final deve vir após a data inicial.',
                                                use_color = True
                                            )
        
        
        
        with Session() as session:  # create session
            
            
            records_period = session.query(ExpensesTable).filter(
                ExpensesTable.data >= start_date,
                ExpensesTable.data <= end_date
                ).order_by(ExpensesTable.data).all()
            
            
            if not records_period:
                print(f'\n{Back.YELLOW}Nenhum registro encontrado na tabela {ExpensesTable.__tablename__} nesse período!{Style.RESET_ALL}')
                
                if not fm.get_confirm(
                        msg = 'Deseja ver outro período? (sim/não): ',
                        yes = 'sim',
                        no = 'não',
                        error_msg = 'opção inválida.',
                        use_color = True):   
                    return
                else:
                    continue

            print(f'\n{Back.CYAN}================== TABELA {ExpensesTable.__tablename__.upper()} =================={Style.RESET_ALL}')
            print(f'{start_date} <-----> {end_date}')
            
            
            # take Columns name
            columns = ExpensesTable.__table__.columns.keys()  # __table__ is a entire table in SQLAlchemy and columns.keys() return a list with columns name
            
            
            # create data list
            table_data = []


            for r in records_period:
                row = []  # create empty list

                for col in columns:  # go through each column name
                    value = getattr(r, col)  # get the value of that column
                    row.append(value)  # add the value to the row
                    
                table_data.append(row)  # add the row to the table data

            # showing the table
            print(tabulate(table_data, headers=columns, tablefmt="fancy_grid"))
        break
            
        
                      
#------------------- MAIN LOOP -------------------

while True:
    
    choice = menu_choice()

    if choice == 1:    # register cost
        option_1()

    elif choice == 2:   # results
        option_2()
        
    elif choice == 3:   # table
        option_3()

    else:
        print(f'\n{Back.WHITE}======= PROGRAMA ENCERRADO ======={Style.RESET_ALL}')
        break


    if not fm.get_confirm(
                        msg = 'Deseja retornar ao menu? (sim/não): ',
                        yes = 'sim',
                        no = 'não',
                        error_msg = 'opção inválida.',
                        use_color = True):    
        print(f'\n{Back.WHITE}======= PROGRAMA ENCERRADO ======={Style.RESET_ALL}')    