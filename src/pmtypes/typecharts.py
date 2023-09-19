from typing import Union
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.pmalchemy.alchemy import Base, session, commit_and_close, get_all_from_table
from src.pmgens.pmgen import PmGen

class PmTypeCharts(Base):
    __tablename__ = 'type_charts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    def __init__(self):
        self.id = self.id

def get_type_chart_table():
    try:
        count = 1
        while count <= 3:
            pm_chart = session.get(PmTypeCharts, count)
            if pm_chart is None:
                pm_chart = PmTypeCharts()
                session.add(pm_chart)
            count += 1
        commit_and_close()
        print("Type chart table ready")
    except Exception as error:
        print(f"Error adding type chart to table: {error}")
        session.rollback()

def getTypeCharts():
    response: Union[PmTypeCharts, None] = get_all_from_table(PmTypeCharts)
    return response

def get_type_chart_for_gen(gen: PmGen):
    if gen is PmGen.GEN1:
        chart = session.get(PmTypeCharts, 1)
    elif gen in [PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
        chart = session.get(PmTypeCharts, 2)
    else:
        chart = session.get(PmTypeCharts, 3)
    return chart
