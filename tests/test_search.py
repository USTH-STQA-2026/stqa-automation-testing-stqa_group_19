"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)

Hints (*Gợi ý*):
    - After logging in, use flutter_fill() to type into the search box
      (*Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm*)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (*Mỗi card sách có role="group" và aria-label chứa thông tin sách*)
    - Use login() helper from conftest.py to log in before testing
      (*Dùng login() helper từ conftest.py để đăng nhập trước khi test*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (*Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.*)

    Hints (*Gợi ý*):
        - login(page, test_config)
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
        - Verify: page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (*Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.*)
    """
    # 1. Đăng nhập vào hệ thống
    login(page, test_config)
    
    # 2. Điền từ khóa tìm kiếm
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
    
    # 3. Đợi Semantics Tree render kết quả (chờ thẻ chứa chữ Flutter xuất hiện)
    result_locator = page.locator('flt-semantics[aria-label*="Flutter"]')
    result_locator.first.wait_for(state="attached", timeout=10000)
    
    # 4. Kiểm tra (Assert) có ít nhất 1 cuốn sách hiển thị
    assert result_locator.count() > 0, "Lỗi: Không tìm thấy sách nào chứa từ khóa 'Flutter'"
    
    # 5. Chụp ảnh màn hình minh chứng
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-04_search_book_by_name.png"))
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (*Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.*)

    Hints (*Gợi ý*):
        - Verify: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (*Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.*)
    """
    # 1. Đăng nhập
    login(page, test_config)
    
    # 2. Tìm kiếm từ khóa không có thật
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "xyz_khong_ton_tai_12345")
    
    # 3. Phải đợi 1 chút để Flutter xóa list sách cũ khỏi UI (Semantics tree update)
    page.wait_for_timeout(2000)
    
    # 4. Lấy danh sách các thẻ sách hiện tại
    book_locator = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    
    # 5. Kiểm tra không còn cuốn sách nào trên màn hình
    assert book_locator.count() == 0, "Lỗi: Vẫn có sách hiển thị dù tìm từ khóa không tồn tại"
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-05_search_book_no_result.png"))
def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → enter "Công nghệ" in the category filter → verify all displayed books
        belong to the "Công nghệ" category.
        (*Đăng nhập → nhập "Công nghệ" vào ô lọc thể loại → kiểm tra tất cả sách
        hiển thị đều thuộc thể loại Công nghệ.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
        - Get book list: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
          (*Lấy danh sách sách*)
        - Loop through each book, verify aria-label contains "Công nghệ"
          (*Lặp qua từng sách, kiểm tra aria-label chứa "Công nghệ"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → enter "Công nghệ" in the category filter → verify all displayed books
        belong to the "Công nghệ" category.
        (*Đăng nhập → nhập "Công nghệ" vào ô lọc thể loại → kiểm tra tất cả sách
        hiển thị đều thuộc thể loại Công nghệ.*)
    """
    login(page, test_config)
    
    # 1. Lọc theo thể loại
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    
    # 2. Đợi danh sách cập nhật
    page.wait_for_timeout(2000)
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    books.first.wait_for(state="attached", timeout=10000)
    
    # 3. Đảm bảo có kết quả để kiểm tra
    count = books.count()
    assert count > 0, "Lỗi: Không có cuốn sách nào được hiển thị sau khi lọc."
    
    # 4. Duyệt qua từng cuốn sách và kiểm tra xem aria-label có chứa "Công nghệ" không
    for i in range(count):
        book_label = books.nth(i).get_attribute("aria-label")
        assert "Công nghệ" in book_label, f"Lỗi: Sách thứ {i+1} không thuộc thể loại Công nghệ. Info: {book_label}"
        
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-06_filter_by_category.png"))
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (*Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.*)

    Hints (*Gợi ý*):
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
        - Verify: page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)

    ✅ COMPLETED

    Description (*Mô tả*):
        Log in → search author name (e.g. "Nguyễn Minh Đức") → verify results found.
        (*Đăng nhập → tìm kiếm tên tác giả → kiểm tra có kết quả.*)
    """
    login(page, test_config)
    
    # 1. Tìm kiếm theo tên tác giả
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
    
    # 2. Đợi kết quả trả về
    result_locator = page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]')
    result_locator.first.wait_for(state="attached", timeout=10000)
    
    # 3. Kiểm tra số lượng kết quả
    assert result_locator.count() > 0, "Lỗi: Không tìm thấy sách của tác giả 'Nguyễn Minh Đức'"
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC-07_search_by_author.png"))
    # pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")
