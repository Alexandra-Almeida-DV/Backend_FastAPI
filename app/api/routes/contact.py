from fastapi import APIRouter, HTTPException
from app.schemas.contact import ContactRequest
from app.services.email_services import send_contact_email

router = APIRouter()

@router.post("/contact")
def send_contact(data: ContactRequest):
    try:
        send_contact_email(data)
        return {"success": True, "message": "Contato enviado com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao enviar contato")
