"""
Logout & Language Tests (*Kiểm thử Đăng xuất & Chuyển ngôn ngữ*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 2 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 2 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - Logout button: 'flt-semantics[role="button"]:has-text("Đăng xuất")'
      (*Nút Đăng xuất*)
    - Language switch EN button: 'flt-semantics[role="button"]:has-text("EN")'
      (*Nút chuyển ngôn ngữ EN*)
    - After logout: page returns to login (has "Đăng nhập" button and "Email" input)
      (*Sau đăng xuất: trang quay về login*)
    - After switching to EN: text "Logout", "Borrow", "Search", "Library" may appear
      (*Sau chuyển EN: text tiếng Anh có thể xuất hiện*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_logout(page, test_config):
    """TC-11: Logout success (*Đăng xuất thành công*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → click Logout → verify page returns to login screen.
        (*Đăng nhập → click Đăng xuất → kiểm tra quay về trang đăng nhập.*)

    Suggested steps (*Gợi ý*):
        1. login(page, test_config)
        2. Find "Đăng xuất" button and click (*Tìm nút "Đăng xuất" và click*)
        3. Wait 3s, re-enable semantics (*Đợi 3s, bật lại semantics*)
        4. Assert: "Đăng nhập" button or Email input exists
           (*Assert: có nút "Đăng nhập" hoặc ô input Email*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    """TC-11: Logout success (*Đăng xuất thành công*)"""
    
    # Bước 1: Tiền điều kiện - Đăng nhập vào hệ thống
    login(page, test_config)

    # Bước 2: Thực hiện hành động - Click nút Đăng xuất
    flutter_click_button(page, "Đăng xuất")

    # Bước 3: Chờ giao diện render và bật lại Semantics Tree
    page.wait_for_timeout(3000)
    enable_flutter_semantics(page)
    
    # (Tùy chọn) Chụp ảnh màn hình để debug/làm bằng chứng report
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc11_logout_success.png"))

    # Bước 4: Test Oracle - Xác minh hệ thống đã quay lại trang Login
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đăng nhập" in sem_text or "Email" in sem_text, \
        "Lỗi: Không tìm thấy giao diện Đăng nhập sau khi bấm Đăng xuất!"
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English (*Chuyển ngôn ngữ sang tiếng Anh*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → click "EN" button → verify UI switches to English.
        (*Đăng nhập → click nút "EN" → kiểm tra giao diện chuyển sang tiếng Anh.*)

    Suggested steps (*Gợi ý*):
        1. login(page, test_config)
        2. Find "EN" button and click (*Tìm nút "EN" và click*)
        3. Wait 2s, re-enable semantics (*Đợi 2s, bật lại semantics*)
        4. Get sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
        5. Assert: "Logout" or "Borrow" or "Library" in sem_text
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    """TC-12: Switch language to English (*Chuyển ngôn ngữ sang tiếng Anh*)"""
    
    # Bước 1: Tiền điều kiện - Đăng nhập vào hệ thống
    login(page, test_config)

    # Bước 2: Thực hiện hành động - Click nút chuyển sang tiếng Anh
    flutter_click_button(page, "EN")

    # Bước 3: Chờ Flutter update state và render lại Semantics
    page.wait_for_timeout(2000)
    enable_flutter_semantics(page)
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc12_switch_language_en.png"))

    # Bước 4 & 5: Test Oracle - Xác minh text trên UI đã chuyển sang tiếng Anh
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    
    # Dùng hàm any() để kiểm tra nếu có ít nhất 1 từ khóa tiếng Anh xuất hiện
    english_keywords = ["Logout", "Borrow", "Search", "Library"]
    has_english_text = any(keyword in sem_text for keyword in english_keywords)
    
    assert has_english_text, \
        f"Lỗi: Giao diện chưa chuyển ngôn ngữ! Text thu được: {sem_text[:200]}..."
