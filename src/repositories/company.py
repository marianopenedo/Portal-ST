from models.company import Company
from schemas.company import CompanySchema
from database.session import db
from sqlalchemy import select

class CompanyRepository():
    def __init__(self):
        self.session = db.get_session()

    def all_company(self):
        return self.session.execute(select(Company)).scalars().all()
    
    def catch_file_path(self, company_id):
        return self.session.execute(select(Company.path_file).where(Company.id == company_id)).scalars().one_or_none()

    def insert_company(self, new_company: CompanySchema) -> Company:
        new_line = Company(**new_company.model_dump(exclude_unset=True))
        self.session.add(new_line)
        self.session.commit()
        self.session.refresh(new_line)
        
        return new_line

    def pending_company(self):
        return self.session.execute(select(Company).where(Company.status == "PENDING")).scalars().all()

    def decision(self, company_id, decision, reason=None) -> None:
        line = self.session.execute(select(Company).where(Company.id == company_id)).scalar()
        line.status = decision
        if reason:
            line.reproval_message = reason

        self.session.commit()

        return {
            'id': line.id,
            'status': line.status,
            'reason': line.reproval_message
        }
        