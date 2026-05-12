import json
import random

def lambda_handler(event, context):

    mensajes = [
        "DevOps pipeline ejecutado correctamente",
        "Microservicio AWS funcionando",
        "Lambda procesó la solicitud exitosamente",
        "Automatización completada",
        "Infraestructura desplegada correctamente"
    ]

    response = {
        "mensaje": random.choice(mensajes),
        "servicio": "microservicio-devops"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
