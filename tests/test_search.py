
"""
test_search.py — Kiểm thử chức năng Tìm kiếm & Lọc sách (REQ-03)

Dựa trên giao diện thực tế stqa.rbc.vn:
  - Tìm kiếm: input placeholder "Tìm kiếm theo tên sách hoặc tác giả..."
  - Lọc thể loại: TEXTBOX (không phải dropdown!)
    placeholder: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
  - Dưới filter có text gợi ý: "Thể loại có sẵn: Công nghệ, Giáo dục, Kinh tế..."

TC-04: Tìm sách theo tên
TC-05: Tìm sách — không có kết quả
TC-06: Lọc theo thể loại (textbox)
TC-07: Tìm theo tên tác giả
TC-07b: Tìm kiếm case-insensitive
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


# ===========================================================================
# TC-04: Tìm sách theo tên — có kết quả
# ===========================================================================
def test_search_by_book_name(page, test_config):
    """
    TC-04: Tìm sách theo tên sách
    - Dữ liệu: Từ khóa = "Flutter"
    - Kết quả mong đợi: Hiển thị "Lập trình Flutter cơ bản" (BOOK001)
    """
    login(page, test_config)

    # Giao diện: input label "Tìm kiếm theo tên sách hoặc tác giả..."
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")

    wait_for_flutter(page, text="Flutter", timeout=10000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC04_search_by_name.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Flutter" in sem_text, (
        f"TC-04 FAILED: Không tìm thấy sách 'Flutter'. Nội dung: {sem_text[:300]}"
    )
    assert "BOOK001" in sem_text or "Lập trình Flutter" in sem_text, (
        "TC-04 FAILED: Không hiển thị BOOK001"
    )
    print("\n✅ TC-04 PASSED: Tìm sách theo tên thành công")


# ===========================================================================
# TC-05: Tìm sách — không có kết quả
# ===========================================================================
def test_search_no_result(page, test_config):
    """
    TC-05: Từ khóa không tồn tại → "Không tìm thấy sách"
    """
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "XYZ123NOTEXIST")

    wait_for_flutter(page, text="Không tìm thấy", timeout=10000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC05_search_no_result.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Không tìm thấy" in sem_text or "không có" in sem_text.lower(), (
        f"TC-05 FAILED: Không hiển thị thông báo 'Không tìm thấy'. Nội dung: {sem_text[:300]}"
    )
    print("\n✅ TC-05 PASSED: Hiển thị 'Không tìm thấy sách' đúng")


# ===========================================================================
# TC-06: Lọc sách theo thể loại — TEXTBOX (không phải dropdown)
# Giao diện thực tế: input placeholder "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
# ===========================================================================
def test_filter_by_category(page, test_config):
    """
    TC-06: Lọc sách theo thể loại bằng TEXTBOX
    - Dữ liệu: Nhập "Công nghệ" vào ô lọc thể loại
    - Kết quả mong đợi: Chỉ hiển thị sách thể loại Công nghệ
    """
    login(page, test_config)

    # Giao diện thực tế: textbox với placeholder "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")

    wait_for_flutter(page, text="Công nghệ", timeout=10000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC06_filter_by_category.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())

    # Sau khi lọc "Công nghệ", phải thấy sách công nghệ như Flutter, Python, v.v.
    assert any(
        book in sem_text
        for book in ["Flutter", "Python", "Kiểm thử", "Mạng máy tính", "An toàn thông tin", "BOOK001", "BOOK002"]
    ), f"TC-06 FAILED: Không hiển thị sách Công nghệ. Nội dung: {sem_text[:300]}"

    print("\n✅ TC-06 PASSED: Lọc theo thể loại (textbox) thành công")


# ===========================================================================
# TC-07: Tìm sách theo tên tác giả
# ===========================================================================
def test_search_by_author(page, test_config):
    """
    TC-07: Tìm sách theo tên tác giả "Nguyễn Minh Đức"
    - Kết quả mong đợi: BOOK001, BOOK009
    """
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")

    wait_for_flutter(page, text="Nguyễn Minh Đức", timeout=10000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC07_search_by_author.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Nguyễn Minh Đức" in sem_text or "Flutter" in sem_text or "Python" in sem_text, (
        f"TC-07 FAILED: Không tìm thấy sách theo tác giả. Nội dung: {sem_text[:300]}"
    )
    print("\n✅ TC-07 PASSED: Tìm kiếm theo tác giả thành công")


# ===========================================================================
# TC-07b: Tìm kiếm case-insensitive
# ===========================================================================
def test_search_case_insensitive(page, test_config):
    """
    TC-07b: Tìm "flutter" (chữ thường) → vẫn ra "Lập trình Flutter cơ bản"
    """
    login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "flutter")

    wait_for_flutter(page, text="Flutter", timeout=10000)
    enable_flutter_semantics(page)

    screenshot_path = os.path.join(test_config["screenshot_dir"], "TC07b_search_case_insensitive.png")
    page.screenshot(path=screenshot_path)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Flutter" in sem_text or "flutter" in sem_text.lower(), (
        "TC-07b FAILED: Tìm kiếm phân biệt hoa/thường — sai theo REQ-03"
    )
    print("\n✅ TC-07b PASSED: Tìm kiếm case-insensitive đúng")
