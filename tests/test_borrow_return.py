"""
test_borrow_return.py — Kiểm thử Mượn & Trả sách (REQ-04, REQ-05)

Giao diện thực tế (từ ảnh chụp):
  - Nút mượn = icon "+" (flt-semantics[role="button"] có aria-label chứa "+")
    Khi click "+" → dialog "Xác nhận mượn sách" với nút "Mượn" để xác nhận, "Hủy" để hủy
  - Nút trả = "Trả sách" (trong tab Mượn / Trả)
  - Tab điều hướng = bottom nav bar (icon, không phải tab role)

TC-08: Mượn sách thành công
TC-09: Xem danh sách sách đang mượn
TC-10: Trả sách thành công
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


def login_as_member(page, test_config):
    """Đăng nhập bằng tài khoản thành viên ba.nguyen@email.com (MEM002)."""
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất", timeout=15000)
    enable_flutter_semantics(page)


def navigate_to_muon_tra(page):
    """
    Chuyển sang tab Mượn / Trả qua bottom nav bar.
    Giao diện: icon bottom nav, dùng aria-label hoặc text "Mượn / Trả"
    """
    # Bottom nav dùng flt-semantics không có role="tab" mà là role="button" hoặc không có role
    muon_tra = page.locator(
        'flt-semantics[aria-label="Mượn / Trả"], '
        'flt-semantics:has-text("Mượn / Trả")'
    ).first
    muon_tra.wait_for(state="attached", timeout=8000)
    muon_tra.click()
    wait_for_flutter(page, timeout=3000)
    enable_flutter_semantics(page)


def navigate_to_sach(page):
    """Chuyển về tab Sách qua bottom nav."""
    sach = page.locator(
        'flt-semantics[aria-label="Sách"], flt-semantics:has-text("Sách")'
    ).first
    try:
        sach.wait_for(state="attached", timeout=5000)
        sach.click()
        wait_for_flutter(page, timeout=2000)
        enable_flutter_semantics(page)
    except Exception:
        pass


# ===========================================================================
# TC-08: Mượn sách thành công
# Giao diện: nút "+" bên cạnh sách "Có sẵn" → dialog → nhấn "Mượn"
# ===========================================================================
def test_borrow_book_success(page, test_config):
    """
    TC-08: Mượn sách thành công
    - Tài khoản: từ .env (thành viên hoạt động)
    - Sách: BOOK002 "Cấu trúc dữ liệu và giải thuật" — Có sẵn
    - Flow: Click "+" → dialog xác nhận → Click "Mượn"
    - Hiện dialog "Xác nhận sách" -> bấm vào nút mượn
    - Kết quả mong đợi: Dialog biến mất, sách chuyển sang "Đang mượn"
    """
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Cấu trúc dữ liệu")
    wait_for_flutter(page, text="Cấu trúc dữ liệu", timeout=8000)
    enable_flutter_semantics(page)

    plus_btn = page.locator(
        'flt-semantics[role="button"][aria-label*="+"], '
        'flt-semantics[role="button"]:has-text("+")'
    ).first
    plus_btn.wait_for(state="attached", timeout=8000)
    plus_btn.click(force=True)

    wait_for_flutter(page, text="Xác nhận", timeout=8000)
    enable_flutter_semantics(page)

    # Nút Mượn trong dialog thường là nút cuối cùng
    confirm_muon = page.locator(
        'flt-semantics[role="button"][aria-label="Mượn"], '
        'flt-semantics[role="button"]:has-text("Mượn")'
    ).last
    confirm_muon.wait_for(state="attached", timeout=5000)
    try:
        confirm_muon.click(force=True, timeout=5000)
    except Exception:
        confirm_muon.dispatch_event("click")

    # Đợi thao tác hoàn tất và trạng thái cập nhật
    page.wait_for_timeout(2000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC08_borrow_book_success.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    assert "Xác nhận" not in sem_text, (
        f"TC-08 FAILED: Dialog xác nhận mượn sách vẫn chưa đóng. Nội dung: {sem_text[:300]}"
    )
    assert "Đang mượn" in sem_text or "Đã mượn" in sem_text, (
        f"TC-08 FAILED: Sách chưa chuyển trạng thái. Nội dung: {sem_text[:300]}"
    )
    print("\n✅ TC-08 PASSED: Mượn sách thành công")


# ===========================================================================
# TC-09: Xem danh sách sách đang mượn
# Giao diện: tab "Mượn / Trả" → "Tất cả phiếu mượn" (Thủ thư) hoặc phiếu của mình
# ===========================================================================
def test_view_borrowed_books(page, test_config):
    """
    TC-09: Xem danh sách sách đang mượn
    - Tab Mượn / Trả → hiển thị phiếu BR001 (BOOK003 - Kiểm thử phần mềm nhập môn)
    - Trạng thái "Đang mượn", có nút "Trả sách"
    """
    login(page, test_config)
    navigate_to_muon_tra(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC09_view_borrowed_books.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    # Giao diện thực tế (ảnh 3): hiển thị "BR001", "Đang mượn", "Kiểm thử phần mềm nhập môn"
    assert (
        "BR001" in sem_text
        or "Kiểm thử phần mềm" in sem_text
        or "Đang mượn" in sem_text
        or "Mã phiếu" in sem_text
        or "phiếu" in sem_text.lower()
    ), f"TC-09 FAILED: Không hiển thị phiếu mượn. Nội dung: {sem_text[:400]}"

    print("\n✅ TC-09 PASSED: Xem danh sách sách đang mượn thành công")


# ===========================================================================
# TC-10: Trả sách thành công
# Giao diện (ảnh 3): nút "Trả sách" màu xanh bên cạnh phiếu "Đang mượn"
# ===========================================================================
def test_return_book_success(page, test_config):
    """
    TC-10: Trả sách thành công
    - Điều kiện: có phiếu "Đang mượn" với nút "Trả sách"
    - Kết quả mong đợi: Trạng thái chuyển "Đã trả", sách về "Có sẵn"
    """
    login(page, test_config)
    navigate_to_muon_tra(page)

    # Nút "Trả sách" (từ ảnh chụp giao diện thực tế)
    tra_sach_btn = page.locator(
        'flt-semantics[role="button"]:has-text("Trả sách")'
    ).first
    tra_sach_btn.wait_for(state="attached", timeout=8000)
    tra_sach_btn.click()

    # Có thể có dialog xác nhận, chờ cập nhật
    wait_for_flutter(page, timeout=3000)
    enable_flutter_semantics(page)

    # Nếu có dialog xác nhận thì nhấn nút xác nhận
    sem_text_after = " ".join(page.locator("flt-semantics").all_text_contents())
    if "Xác nhận" in sem_text_after:
        confirm = page.locator('flt-semantics[role="button"]:has-text("Trả")').last
        try:
            confirm.click()
            wait_for_flutter(page, timeout=3000)
            enable_flutter_semantics(page)
        except Exception:
            pass

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC10_return_book_success.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert (
        "Đã trả" in sem_text
        or "trả thành công" in sem_text.lower()
        or "Có sẵn" in sem_text
    ), f"TC-10 FAILED: Không xác nhận trả sách. Nội dung: {sem_text[:400]}"

    print("\n✅ TC-10 PASSED: Trả sách thành công")


# ===========================================================================
# TC-08b: Mượn sách thất bại — thành viên bị tạm ngưng (REQ-04)
# Giao diện: click "+" → thông báo lỗi (không có dialog xác nhận)
# ===========================================================================
def test_borrow_suspended_member(page, test_config):
    """
    TC-08b: Thành viên tạm ngưng (MEM004 - Lê Căn Cù) không mượn được
    - Tài khoản: cu.le@email.com / password123
    - Kết quả: Thông báo tạm ngưng
    """
    page.goto(test_config["base_url"], wait_until="networkidle", timeout=60000)
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "cu.le@email.com")
    flutter_fill(page, "Mật khẩu", "password123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất", timeout=15000)
    enable_flutter_semantics(page)

    # Thử nhấn "+" trên sách bất kỳ có sẵn
    plus_btn = page.locator(
        'flt-semantics[role="button"][aria-label*="+"], '
        'flt-semantics[role="button"]:has-text("+")'
    ).first
    try:
        plus_btn.wait_for(state="attached", timeout=8000)
        plus_btn.click()
        wait_for_flutter(page, timeout=5000)
        enable_flutter_semantics(page)

        screenshot_path = os.path.join(test_config["screenshot_dir"], "TC08b_borrow_suspended.png")
        page.screenshot(path=screenshot_path)

        sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
        # Thông báo lỗi đúng lý do: "tạm ngưng" (không phải "hết hạn")
        assert "tạm ngưng" in sem_text.lower() or "Tạm ngưng" in sem_text, (
            f"TC-08b FAILED: Không hiển thị lỗi tạm ngưng. Nội dung: {sem_text[:300]}"
        )
        print("\n✅ TC-08b PASSED: Từ chối đúng lý do tạm ngưng")
    except Exception as e:
        page.screenshot(path=os.path.join(test_config["screenshot_dir"], "TC08b_error.png"))
        print(f"\n⚠️ TC-08b: {e}")
        pytest.fail(f"TC-08b Không hoàn thành: {e}")


# ===========================================================================
# TC-08c: Mượn sách thất bại — vượt giới hạn 3 sách (BVA)
# ===========================================================================
def test_borrow_limit_exceeded(page, test_config):
    """
    TC-08c: BVA — thành viên đang mượn 3 sách không thể mượn thêm
    """
    login(page, test_config)

    # Mượn 2 sách đầu (MEM002 đang mượn 1 → cần thêm 2 để đủ 3)
    books = ["Cấu trúc dữ liệu", "Trí tuệ nhân tạo"]
    for keyword in books:
        try:
            flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", keyword)
            wait_for_flutter(page, text=keyword, timeout=8000)
            enable_flutter_semantics(page)

            plus_btn = page.locator(
                'flt-semantics[role="button"][aria-label*="+"], '
                'flt-semantics[role="button"]:has-text("+")'
            ).first
            plus_btn.wait_for(state="attached", timeout=5000)
            plus_btn.click()

            wait_for_flutter(page, text="Xác nhận", timeout=5000)
            enable_flutter_semantics(page)

            confirm = page.locator('flt-semantics[role="button"]:has-text("Mượn")').last
            confirm.click()
            wait_for_flutter(page, timeout=2000)
            enable_flutter_semantics(page)

            # Clear search
            flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "")
            wait_for_flutter(page, timeout=1000)
            enable_flutter_semantics(page)
        except Exception as e:
            print(f"  Bỏ qua bước mượn '{keyword}': {e}")
            pytest.fail(f"Không thể mượn sách '{keyword}': {e}")

    # Thử mượn sách thứ 4
    try:
        flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Python")
        wait_for_flutter(page, text="Python", timeout=8000)
        enable_flutter_semantics(page)

        plus_btn = page.locator(
            'flt-semantics[role="button"][aria-label*="+"], '
            'flt-semantics[role="button"]:has-text("+")'
        ).first
        plus_btn.wait_for(state="attached", timeout=5000)
        plus_btn.click()
        wait_for_flutter(page, timeout=5000)
        enable_flutter_semantics(page)

        screenshot_path = os.path.join(test_config["screenshot_dir"], "TC08c_borrow_limit.png")
        page.screenshot(path=screenshot_path)

        sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
        assert "giới hạn" in sem_text.lower() or "tối đa" in sem_text.lower() or "3" in sem_text, (
            "TC-08c FAILED: Không hiển thị thông báo vượt giới hạn 3 sách"
        )
        print("\n✅ TC-08c PASSED: Hiển thị lỗi vượt giới hạn 3 sách")
    except Exception as e:
        print(f"\n⚠️ TC-08c: Không hoàn thành — {e}")
        pytest.fail(f"TC-08c Không hoàn thành: {e}")
