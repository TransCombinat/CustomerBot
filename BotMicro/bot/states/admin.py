from aiogram.fsm.state import State, StatesGroup


class LoginState(StatesGroup):
    access_key = State()


class NewAdminState(StatesGroup):
    name = State()
