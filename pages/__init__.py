from .login_page import LoginPage
from .logout_page import LogoutPage
from .purchase_page import PurchasePage

PAGE_CLASSES = {
    'login': LoginPage,
    'logout': LogoutPage,
    'purchase': PurchasePage
}
