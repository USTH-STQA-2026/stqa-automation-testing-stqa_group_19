"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)
"""
import os
import re
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    wait_for_flutter, SCREENSHOT_DIR,
)

# ---------------------------------------------------------------------------
# Local Domain Helpers — Các hàm hỗ trợ đặc thù cho Mượn/Trả sách
# ---------------------------------------------------------------------------

def _sync_flutter_ui(page, delay_ms: int = 1000):
    """
    Chờ hiệu ứng Animation của Flutter hoàn tất và ép render lại Semantics Tree.
    Giúp tránh tình trạng Playwright tương tác với DOM ảo cũ.
    """
    page.wait_for_timeout(delay_ms)
    enable_flutter_semantics(page)


def _click_exact_button(page, text: str):
    """
    Click vào một nút bấm có text khớp TUYỆT ĐỐI (Dùng Regex).
    Tránh lỗi click nhầm nút 'Mượn sách này' khi muốn click nút 'Mượn' trên dialog.
    """
    exact_btn = page.locator('flt-semantics[role="button"]').filter(
        has_text=re.compile(f"^{text}$")
    )
    exact_btn.click()


def _check_text_exists_on_screen(page, *expected_texts) -> bool:
    """
    Quét toàn bộ text đang hiển thị trên giao diện (bất chấp cấu trúc cây DOM).
    Trả về True nếu ít nhất một trong các expected_texts xuất hiện.
    """
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    return any(text in sem_text for text in expected_texts)


def _login_with_account(page, base_url: str, email: str, password: str):
    """Đăng nhập bằng một tài khoản cụ thể và chờ giao diện load xong."""
    page.goto(base_url, wait_until="domcontentloaded", timeout=60000)
    page.locator("flt-glass-pane").wait_for(state="attached", timeout=45000)
    enable_flutter_semantics(page)
    
    flutter_fill(page, "Email", email)
    flutter_fill(page, "Mật khẩu", password)
    flutter_click_button(page, "Đăng nhập")
    
    wait_for_flutter(page, text="Đăng xuất")
    enable_flutter_semantics(page)


# ---------------------------------------------------------------------------
# Test Cases — Kịch bản kiểm thử chính
# ---------------------------------------------------------------------------

def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book (*Mượn sách có trạng thái 'Có sẵn'*)"""
    # 1. Đăng nhập bằng tài khoản chưa mượn sách nào (độc lập dữ liệu)
    _login_with_account(page, test_config["base_url"], "dam.tran@email.com", "password123")

    # 2. Click mượn cuốn sách đầu tiên hiển thị
    borrow_btn = page.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').first
    borrow_btn.wait_for(state="attached", timeout=10000)
    borrow_btn.click()

    # 3. Đồng bộ UI để Dialog xác nhận xuất hiện
    _sync_flutter_ui(page, delay_ms=1000)

    # 4. Click chính xác vào nút "Mượn" trên Dialog
    _click_exact_button(page, text="Mượn")

    # 5. Chờ API xử lý và đồng bộ lại UI
    _sync_flutter_ui(page, delay_ms=2000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc08_borrow_book.png"))

    # 6. Kiểm tra kết quả
    is_success = _check_text_exists_on_screen(page, "Đang mượn", "thành công")
    assert is_success, "Lỗi: Không hiển thị trạng thái 'Đang mượn' hoặc thông báo thành công sau khi mượn."


def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)"""
    # 1. Đăng nhập bằng tài khoản ĐÃ có sẵn sách đang mượn
    _login_with_account(page, test_config["base_url"], "ba.nguyen@email.com", "password123")

    # 2. Chuyển sang tab "Mượn / Trả"
    tab = page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
    tab.click()
    
    _sync_flutter_ui(page, delay_ms=1000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc09_view_borrowed.png"))

    # 3. Kiểm tra kết quả
    has_borrowed_label = _check_text_exists_on_screen(page, "Đang mượn")
    has_return_btn = page.locator('flt-semantics[role="button"]:has-text("Trả sách")').count() > 0
    
    assert has_borrowed_label or has_return_btn, "Lỗi: Không tìm thấy sách đang mượn nào trong tab 'Mượn / Trả'."


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)"""
    # 1. Đăng nhập bằng tài khoản ĐÃ có sẵn sách đang mượn
    _login_with_account(page, test_config["base_url"], "ba.nguyen@email.com", "password123")

    # 2. Chuyển sang tab "Mượn / Trả"
    tab = page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
    tab.click()
    
    _sync_flutter_ui(page, delay_ms=1000)

    # 3. Click nút "Trả sách" đầu tiên
    return_btn = page.locator('flt-semantics[role="button"]:has-text("Trả sách")').first
    return_btn.wait_for(state="attached", timeout=10000)
    return_btn.click()

    # 4. Chờ API xử lý việc trả sách
    _sync_flutter_ui(page, delay_ms=2000)
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc10_return_book.png"))

    # 5. Kiểm tra kết quả (Sách về lại 'Có sẵn' hoặc mất hẳn nút 'Trả sách' cũ)
    is_success_msg = _check_text_exists_on_screen(page, "Có sẵn", "thành công")
    no_return_btn_left = page.locator('flt-semantics[role="button"]:has-text("Trả sách")').count() == 0
    
    assert is_success_msg or no_return_btn_left, "Lỗi: Thao tác trả sách thất bại, sách không đổi trạng thái."