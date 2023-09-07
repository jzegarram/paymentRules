from config.fields import fields
from config.metadata import operators, actionTypes
from config.rules.mercadoPago import mercadoPago_Rule
from config.rules.niubiz import niubiz_Rule
from config.rules.pagoEfectivo import pagoEfectivo_Rule
from config.rules.culqui import culqi_Rule
from config.rules.ebanx import ebanx_Rule
from config.rules.payu import payU_Rule
from utils.asking import ask_questions
from ruleMachine import ruleMachine

def main():
    paymentRules = [mercadoPago_Rule, niubiz_Rule, culqi_Rule, ebanx_Rule, payU_Rule, pagoEfectivo_Rule]
    userAnswers = ask_questions(fields)

    available_gateways = ruleMachine(paymentRules, userAnswers, operators, actionTypes)
    print("\n===================================================")
    print("\nPuede utilizar las siguientes PASARELAS de pago:\n")
    for index, action in enumerate(available_gateways, start=1):
        print(f"{index}. {action}")

if __name__ == "__main__":
    main()
