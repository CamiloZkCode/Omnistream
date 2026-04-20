# domain/descuento_client.py
import httpx
from typing import Optional


class DescuentoServiceClient:
    """
    Cliente para consumir el microservicio de descuentos.
    Implementa el patrón Strangler Fig: desvía las llamadas de descuento
    al nuevo microservicio en lugar de usar la lógica local.
    """
    
    def __init__(self, base_url: str = "http://localhost:8001", timeout: float = 5.0):
        self.base_url = base_url
        self.timeout = timeout
    
    def calcular(self, precio_base: float, codigo_vip: Optional[str], antiguedad: int) -> float:
        """
        Llama al microservicio para calcular el precio con descuento.
        
        Args:
            precio_base: Precio base del servicio
            codigo_vip: Código VIP (None o string vacío = sin VIP)
            antiguedad: Meses de antigüedad
        
        Returns:
            Precio final con descuentos aplicados
        """
        with httpx.Client(timeout=self.timeout) as client:
            response = client.post(
                f"{self.base_url}/api/v1/calcular-descuento",
                json={
                    "precio_base": precio_base,
                    "tiene_codigo_vip": bool(codigo_vip),
                    "antiguedad": antiguedad
                }
            )
            response.raise_for_status()
            data = response.json()
            return data["precio_final"]
    
    def health_check(self) -> bool:
        """Verifica si el microservicio está disponible"""
        try:
            with httpx.Client(timeout=2.0) as client:
                response = client.get(f"{self.base_url}/health")
                return response.status_code == 200
        except Exception:
            return False