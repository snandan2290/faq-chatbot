import neuro_san
from services.neuro_san_service import NeuroSANService

print("Neuro-SAN Installed Successfully")

service = NeuroSANService()

print(service.ask("How do I change my bank account?"))
