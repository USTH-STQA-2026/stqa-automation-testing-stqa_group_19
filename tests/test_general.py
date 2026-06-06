
"""
test_general.py — Kiểm thử chức năng chung

Giao diện thực tế (từ ảnh chụp):
  - Nút đăng xuất: icon ở góc phải AppBar (không phải text "Đăng xuất")
    → aria-label thường là "Đăng xuất" hoặc icon logout
  - Màn hình login sau logout: có text "Đăng nhập" + "Tài khoản thử nghiệm:"
    (KHÔNG có label "Email" / "Mật khẩu" trực tiếp trong semantics khi chưa focus)
  - Chuyển ngôn ngữ: nút "EN" ở AppBar (đã có sẵn, không phải dropdown)
  - Tab Thành viên: bottom nav bar (icon + text "Thành viên")
  - Form thêm thành viên: label "Họ và tên", "Email", "Số điện thoại", nút "Thêm thành viên"
  - Thêm thành viên: navigate sang màn hình riêng (AppBar title "Thêm thành viên mới")

TC-11: Đăng xuất
TC-12: Chuyển ngôn ngữ sang EN
TC-13: Thêm thành viên mới (REQ-07)
TC-14: Thêm thành viên email trùng (REQ-07)
"""

import os
import pytest
from conftest import (
    enable_flutter_semantics,
    flutter_fill,
    flutter_click_button,
    wait_for_flutter,
    login,
)


def login_as_librarian(page, test_config):
    """Đăng nhập Thủ thư."""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất", timeout=15000)
    enable_flutter_semantics(page)


def navigate_to_thanh_vien(page):
    """
    Chuyển sang tab Thành viên qua bottom nav bar.
    Giao diện: icon bottom nav với text/aria-label "Thành viên"
    """
    tv_nav = page.locator(
        'flt-semantics[aria-label="Thành viên"], '
        'flt-semantics:has-text("Thành viên")'
    ).first
    tv_nav.wait_for(state="attached", timeout=8000)
    tv_nav.click()
    wait_for_flutter(page, timeout=3000)
    enable_flutter_semantics(page)


# ===========================================================================
# TC-11: Đăng xuất
# Giao diện: icon logout ở góc phải AppBar
# Sau logout: màn hình login hiện "Đăng nhập" + "Tài khoản thử nghiệm:"
# ===========================================================================
def test_logout(page, test_config):
    """
    TC-11: Đăng xuất thành công
    - Nhấn icon đăng xuất (góc phải AppBar)
    - Kết quả mong đợi: Về màn hình đăng nhập (có text "Đăng nhập")
    """
    login(page, test_config)

    # Icon đăng xuất ở AppBar — thử nhiều cách locate
    # Từ error log: sau logout thấy "VIENĐăng nhậpTài khoản thử nghiệm:"
    # → màn hình login hiển thị đúng, chỉ cần assert "Đăng nhập" + không có "Đăng xuất" icon
    logout_btn = page.locator(
        'flt-semantics[aria-label="Đăng xuất"], '
        'flt-semantics[role="button"][aria-label*="xuất"], '
        'flt-semantics[role="button"]:has-text("Đăng xuất")'
    ).first
    logout_btn.wait_for(state="attached", timeout=8000)
    logout_btn.click()

    # Chờ màn hình login xuất hiện
    wait_for_flutter(page, text="Đăng nhập", timeout=10000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC11_logout.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    # Từ error log biết rằng màn hình login có: "Đăng nhập", "Tài khoản thử nghiệm:"
    # Assert: đã về màn hình login
    assert "Đăng nhập" in sem_text, (
        f"TC-11 FAILED: Không về màn hình đăng nhập. Nội dung: {sem_text[:200]}"
    )
    # Assert: không còn ở trang chính (không có bottom nav "Sách", "Mượn / Trả")
    # Hoặc đơn giản: input đăng nhập khả dụng
    assert (
        "Tài khoản" in sem_text
        or "thử nghiệm" in sem_text.lower()
        or page.locator('input[aria-label="Email"]').count() > 0
    ), f"TC-11 FAILED: Màn hình login không hiển thị đúng. Nội dung: {sem_text[:200]}"

    print("\n✅ TC-11 PASSED: Đăng xuất thành công")


# ===========================================================================
# TC-12: Chuyển ngôn ngữ sang EN
# Giao diện: nút "EN" ở AppBar (góc phải, cạnh "VI" đang active)
# ===========================================================================
def test_switch_language_to_en(page, test_config):
    """
    TC-12: Nhấn nút "EN" trên AppBar để chuyển sang tiếng Anh
    - Kết quả mong đợi: Giao diện chuyển sang tiếng Anh (Logout, Books, Borrow...)
    """
    login(page, test_config)

    # Nút "EN" trên AppBar (từ ảnh: "✓ VI" và "EN" là 2 nút cạnh nhau)
    en_btn = page.locator(
        'flt-semantics[role="button"]:has-text("EN"), '
        'flt-semantics[aria-label="EN"]'
    ).first
    en_btn.wait_for(state="attached", timeout=8000)
    en_btn.click()

    wait_for_flutter(page, timeout=3000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC12_switch_language_en.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    english_keywords = ["Logout", "Books", "Borrow", "Search", "Members", "Return", "Library"]
    has_english = any(kw in sem_text for kw in english_keywords)

    assert has_english, (
        f"TC-12 FAILED: Giao diện không chuyển sang tiếng Anh. Nội dung: {sem_text[:300]}"
    )
    print("\n✅ TC-12 PASSED: Chuyển ngôn ngữ sang EN thành công")
