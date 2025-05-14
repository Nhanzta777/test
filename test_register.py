from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import unittest

class TestRegister(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://nhanzta777.github.io/MKMOVIES/")
        self.wait = WebDriverWait(self.driver, 10)
        
    def test_register_and_login(self):
        test_case = {
            'id': 'TC001',
            'description': 'Register and login with new account',
            'fullname': 'Le Viet Nhan',
            'email': 'levietnhan300@gmail.com',
            'password': 'Levietnhan300!',
            'confirm_password': 'Levietnhan300!',
            'expected_result': 'Đăng ký và đăng nhập thành công'
        }
        
        try:
            print("Bắt đầu test đăng ký và đăng nhập...")
            
            print("Đang tìm nút Đăng ký ngay...")
            try:
                register_link = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='Đăng ký ngay']"))
                )
                self.driver.execute_script("arguments[0].click();", register_link)
                time.sleep(3)
                print("Đã click vào link Đăng ký ngay")
            except Exception as e:
                print(f"Lỗi khi click link đăng ký: {str(e)}")
                raise
            
            print("Đang điền thông tin đăng ký...")
            
            try:
                fullname_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "register-name"))
                )
                fullname_field.clear()
                fullname_field.send_keys(test_case['fullname'])
                time.sleep(1)
                print(f"Đã điền họ tên: {test_case['fullname']}")
            except Exception as e:
                print(f"Lỗi khi điền họ tên: {str(e)}")
                raise
            
            try:
                email_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "register-email"))
                )
                email_field.clear()
                email_field.send_keys(test_case['email'])
                time.sleep(1)
                print(f"Đã điền email: {test_case['email']}")
            except Exception as e:
                print(f"Lỗi khi điền email: {str(e)}")
                raise
            
            try:
                password_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "register-password"))
                )
                password_field.clear()
                password_field.send_keys(test_case['password'])
                time.sleep(1)
                print("Đã điền mật khẩu")
            except Exception as e:
                print(f"Lỗi khi điền mật khẩu: {str(e)}")
                raise
            
            try:
                confirm_password_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "register-confirm-password"))
                )
                confirm_password_field.clear()
                confirm_password_field.send_keys(test_case['confirm_password'])
                time.sleep(1)
                print("Đã điền xác nhận mật khẩu")
            except Exception as e:
                print(f"Lỗi khi điền xác nhận mật khẩu: {str(e)}")
                raise
            
            print("Đang click nút đăng ký...")
            try:
                submit_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Đăng ký']"))
                )
                self.driver.execute_script("arguments[0].click();", submit_button)
                time.sleep(2)
                print("Đã click nút đăng ký")
            except Exception as e:
                print(f"Lỗi khi click nút submit: {str(e)}")
                raise
            
            time.sleep(3)
            
            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                self.assertEqual(alert_text, "Đăng ký thành công! Vui lòng đăng nhập.")
                alert.accept()
                print("Đăng ký thành công!")
            except Exception as e:
                print(f"Lỗi khi kiểm tra thông báo đăng ký: {str(e)}")
                raise

            print("\nBắt đầu test đăng nhập...")
            
            print("Đang điền email đăng nhập...")
            try:
                email_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "login-email"))
                )
                email_field.clear()
                email_field.send_keys(test_case['email'])
                time.sleep(1)
                print(f"Đã điền email: {test_case['email']}")
            except Exception as e:
                print(f"Lỗi khi điền email đăng nhập: {str(e)}")
                raise
            
            print("Đang điền mật khẩu đăng nhập...")
            try:
                password_field = self.wait.until(
                    EC.presence_of_element_located((By.ID, "login-password"))
                )
                password_field.clear()
                password_field.send_keys(test_case['password'])
                time.sleep(1)
                print("Đã điền mật khẩu")
            except Exception as e:
                print(f"Lỗi khi điền mật khẩu đăng nhập: {str(e)}")
                raise
            
            print("Đang click nút đăng nhập...")
            try:
                submit_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Đăng nhập']"))
                )
                self.driver.execute_script("arguments[0].click();", submit_button)
                time.sleep(2)
                print("Đã click nút đăng nhập")
            except Exception as e:
                print(f"Lỗi khi click nút đăng nhập: {str(e)}")
                raise
            
            time.sleep(3)
            
            try:
                current_url = self.driver.current_url
                self.assertTrue('home.html' in current_url, "Không chuyển đến trang chủ sau khi đăng nhập")
                print(f"\nTest Case {test_case['id']}: {test_case['description']}")
                print("Trạng thái: PASSED")
                print(f"Kết quả: {test_case['expected_result']}")
            except Exception as e:
                print(f"\nTest Case {test_case['id']}: {test_case['description']}")
                print("Trạng thái: FAILED")
                print(f"Lỗi: {str(e)}")
                raise
            
            print("\nĐang đợi 10 giây để xem kết quả...")
            time.sleep(10)
            
        except Exception as e:
            print(f"\nTest Case {test_case['id']}: {test_case['description']}")
            print("Trạng thái: FAILED")
            print(f"Lỗi: {str(e)}")
            print("\nĐang đợi 10 giây để xem lỗi...")
            time.sleep(10)
            raise
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 