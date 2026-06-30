"""
Author: Julio Cesar Lopez Sanchez
Problema: Escribe un programa en Python para crear una clase 
          «BankAccount» con un atributo «balance» y dos métodos: 
          «deposit(amount)», que añade fondos al saldo, 
          y «withdraw(amount)», que deduce fondos pero evita que el saldo sea inferior a cero.
"""


class BankAccount:
    """Representa una cuenta bancaria con un balance y métodos para depositar y retirar fondos."""

    def __init__(self, balance: float) -> None:
        """
        Inicializa la cuenta bancaria con un balance inicial.

        Args:
            balance (float): El balance inicial de la cuenta. Debe ser mayor o igual a cero.
        Raises:
            ValueError: Si el balance inicial es negativo.
        """
        if balance < 0:
            raise ValueError("El balance inicial no puede ser negativo.")
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposita fondos en la cuenta.

        Args:
            amount (float): El monto a depositar. Debe ser mayor a 0.

        Raises:
            ValueError: Si el monto a depositar es menor o igual a 0.
        """
        if amount <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Retira fondos de la cuenta.

        Args:
            amount (float): El monto a retirar. Debe ser mayor a 0.

        Raises:
            ValueError: Si el monto a retirar es menor o igual a 0 o si no hay suficientes fondos.
        """
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if self.balance < amount:
            raise ValueError(f"Fondos insuficientes. Tu saldo actual es: {self.balance}")
        self.balance -= amount


def main() -> None:
    """Funcion principal"""
    account1 = BankAccount(1500)
    print(f"Tu saldo actual es: {account1.balance}")

    account1.deposit(500)
    print(f"Tu saldo actual es: {account1.balance}")

    account1.withdraw(1000)
    print(f"Tu saldo actual es: {account1.balance}")

if __name__ == "__main__":
    main()
