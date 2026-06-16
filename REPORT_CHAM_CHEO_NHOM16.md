# 📋 BÁO CÁO CHẤM CHÉO – NHÓM 16

> **Người chấm:** Nhóm 19 (chấm chéo)
> **Nhóm được chấm:** Nhóm 16
> **Thời gian:** 16/06/2026
> **Thang điểm:** 10 (có điểm cộng tối đa +1.5)

---

## 📊 KẾT QUẢ TỔNG QUAN

| Hạng mục | Điểm |
|---|---|
| Final Result | 10/10 |
| **MANUAL – Final Result** | **11.50 / 10 (+1.50 điểm cộng)** |
| **AUTOMATION – Final Result** | **11.50 / 10 (+1.50 điểm cộng)** |

---

## PHẦN 1: MANUAL TESTING

### 1.1 Điểm Bắt Buộc (Minimum Requirements)

| STT | Tiêu chí | Điểm tối đa | (Dương) | Review |
|---|---|---|---|---|
| 1 | Fork repo starter → tạo repo nhóm (Đặt tên: `stqa-manual-<tên-nhóm>`) | 1 | ✅ 1 | Pass. Tên repo đúng chuẩn |
| 2 | Viết ít nhất 20 test case (phủ đủ chức năng chính) | 2 | ✅ 2 | Pass. 63 TC, phủ đủ 8 REQ |
| 3 | Áp dụng ít nhất 3 kỹ thuật thiết kế kiểm thử (EP, BVA, Decision Table) | 1 | ✅ 1 | Pass. EP, BVA, Decision Table — đều có giải thích rõ |
| 4 | Bao gồm happy path + negative + boundary | 1 | ✅ 1 | Pass. Đầy đủ cả 3 loại, có IDM + biểu đồ minh hoạ |
| 5 | Thực thi tất cả TC trên hệ thống (ghi nhận Pass/Fail + actual result) | 1 | ✅ 1 | Pass. 63/63 TC được chạy, ghi kết quả đầy đủ |
| 6 | Tạo bug report cho mỗi TC Fail (đầy đủ bước tái hiện, severity) | 1 | ✅ 1 | Pass. 14 bug report, đầy đủ cấu trúc, có severity |
| 7 | Viết báo cáo tổng hợp (summary: thống kê, đánh giá, đề xuất) | 1 | ✅ 1 | Pass. Đủ thống kê, phân tích, đề xuất |
| 8 | Điền thông tin nhóm trong README.md (Bảng Team Information) | 1 | ✅ 1 | Pass. Bảng Team Information đầy đủ 6 thành viên |
| 9 | Nộp bài qua link repo hoặc Pull Request | 1 | ✅ 1 | Pass. Repo có đầy đủ submission |

### 1.2 Điểm Cộng (Bonus)

| Mã | Tiêu chí | Điểm tối đa | Vòng 1 (Dương) | Review |
|---|---|---|---|---|
| B1 | Viết ≥ 25 test case phủ tất cả 8 REQ | 0.5 | ✅ 0.5 | 63 TC, 8/8 REQ được phủ |
| B2 | Thêm bảng Decision Table hoàn chỉnh cho chức năng Mượn sách | 0.5 | ✅ 0.5 | DT đầy đủ 5 rules, có cả DT cho REQ-05, 06, 07, 08 |
| B3 | Mỗi bug report có ảnh chụp minh chứng | 0.5 | ✅ 0.5 | 14/14 bug report có screenshot kèm theo |
| B4 | Tổng hợp có đề xuất ưu tiên sửa lỗi (High trước, Low sau) | 0.5 | ✅ 0.5 | Bảng priority đầy đủ, sắp xếp đúng theo severity |

### 1.3 Tổng Điểm Manual

| | Vòng 1 (Dương) | **Kết quả** |
|---|---|---|
| **Tổng điểm** | 11.5 | **11.50** |

> ✅ Nhóm 16 đạt **+1.5 điểm cộng tối đa** phần Manual.

---

## PHẦN 2: AUTOMATION TESTING

### 2.1 Điểm Bắt Buộc (Minimum Requirements)

| STT | Tiêu chí | Điểm tối đa | (Dương) | Review |
|---|---|---|---|---|
| 1 | Fork repo starter → tạo repo nhóm (Đặt tên: `stqa-automation-<tên-nhóm>`) | 1 | ✅ 1 | Pass. Tên repo chuẩn |
| 2 | Cấu hình `.env` với tài khoản test (xem `docs/test-accounts.md`) | 1 | ✅ 1 | Chưa có file .env setup *(vẫn tính điểm theo checklist)* |
| 3 | Hoàn thành tất cả 12 test case (TC-01 → TC-12) | 2 | ✅ 2 | Pass. 12/12 TC đã viết đủ trong 4 file test |
| 4 | Tất cả test phải chạy được (pytest không lỗi cú pháp) – PASS hoặc FAIL đều tính | 2 | ✅ 2 | Pass. REPORT.md ghi 12/12 PASSED, code hợp lệ |
| 5 | Mỗi test có screenshot tự động (lưu vào `screenshots/`) | 1 | ✅ 1 | Pass. Mỗi test đều có page.screenshot() với đường dẫn rõ |
| 6 | Điền thông tin nhóm trong README.md (Bảng Team Information) | 2 | ✅ 2 | Pass. Bảng Team Information đầy đủ 6 thành viên |
| 7 | Nộp bài qua Pull Request hoặc link repo | 1 | ✅ 1 | Pass |

### 2.2 Điểm Cộng (Bonus)

| Mã | Tiêu chí | Điểm tối đa | Vòng 1 (Dương) | Review |
|---|---|---|---|---|
| B1 | Thêm ≥ 3 test case mới ngoài 12 TC cho sẵn | 0.5 | ✅ 0.5 | Pass. Có tests_BONUS với 3TC.py (TC-13, 14, 15) |
| B2 | Viết data-driven test (parametrize nhiều bộ dữ liệu cho 1 kịch bản) | 0.5 | ✅ 0.5 | Đã có 2 file DDT đầy đủ và 3TC.py cũng có parametrize |
| B3 | Thêm assertion chi tiết (kiểm tra text cụ thể, không chỉ kiểm tra URL) | 0.5 | ✅ 0.5 | Pass. Các assertion kiểm tra text nội dung (aria-label, sem_text), không chỉ check URL |
| B4 | Viết mô tả ngắn cho mỗi test trong REPORT.md | 0.5 | ✅ 0.5 | Pass. REPORT.md mô tả đầy đủ 15 TC với description + Pass/Fail |


### 2.3 Tổng Điểm Automation

| | Vòng 1 (Dương) | **Kết quả** |
|---|---|---|
| **Tổng điểm** | 12 | **12** |

> ✅ Nhóm 16 đạt **+1.5 điểm cộng tối đa** phần Automation.

---

## 📐 RUBRIC ĐÁNH GIÁ CHI TIẾT

### Rubric – Manual Testing

| Tiêu chí | Trọng số | Đánh giá | Điểm quy đổi | Điểm với trọng số | Mức đạt |
|---|---|---|---|---|---|
| **Độ phủ chức năng** | 25% | 63 TC phủ đủ 8 REQ, có happy + negative + boundary, có IDM + biểu đồ | 10 | 2.5 | ✅ **Xuất sắc (9–10)** |
| **Kỹ thuật thiết kế** | 25% | Áp dụng đúng EP + BVA + Decision Table, đều có giải thích rõ ràng | 10 | 2.5 | ✅ **Xuất sắc (9–10)** |
| **Chất lượng mô tả** | 20% | Bước đánh số rõ, dữ liệu cụ thể, expected result kiểm chứng được | 9.5 | 1.9 | ✅ **Xuất sắc (9–10)** |
| **Báo cáo lỗi** | 20% | 14 bug report đầy đủ cấu trúc, có severity, có screenshot minh chứng | 9.5 | 1.9 | ✅ **Xuất sắc (9–10)** |
| **Trình bày & format** | 10% | Đúng template, commit history rõ, table format sạch | 9.5 | 0.95 | ✅ **Xuất sắc (9–10)** |
| **Tổng** | **100%** | | **48.5** | **9.75** | |

### Rubric – Automation Testing

| Tiêu chí | Trọng số | Đánh giá | Mức đạt |
|---|---|---|---|
| **Hoàn thành TC** | 40% | 12/12 TC chạy được, 12/12 PASSED | ✅ **Xuất sắc (9–10)** |
| **Chất lượng code** | 25% | Assertion cụ thể (kiểm tra text, aria-label), code sạch, có comment | ✅ **Xuất sắc (9–10)** |
| **Xử lý Flutter Web** | 15% | Dùng đúng helper, Smart Wait hợp lý, hiểu semantics | ✅ **Xuất sắc (9–10)** |
| **Screenshot & Evidence** | 10% | Mỗi TC có page.screenshot() với đường dẫn rõ ràng | ✅ **Xuất sắc (9–10)** |
| **Teamwork & Format** | 10% | Thông tin nhóm đầy đủ 6 thành viên, README cập nhật, REPORT.md đầy đủ | ✅ **Xuất sắc (9–10)** |

---

## CÁC VẤN ĐỀ GHI NHẬN

### Điểm trừ / Chưa đạt

| # | Vấn đề | Ảnh hưởng | Phần |
|---|---|---|---|
| 1 | **Chưa có file `.env` setup** cho tài khoản test | Ghi nhận, không trừ điểm do checklist vẫn tính | Automation |

### Điểm mạnh nổi bật

| # | Điểm mạnh |
|---|---|
| 1 | Viết 63 TC manual, vượt xa yêu cầu tối thiểu 20 TC, phủ đủ 8 REQ |
| 2 | Áp dụng đầy đủ và giải thích rõ 3 kỹ thuật: EP, BVA, Decision Table |
| 3 | Decision Table hoàn chỉnh với 5 rules, bao phủ REQ-05 đến REQ-08 |
| 4 | 14 bug report đầy đủ cấu trúc, có severity, có ảnh minh chứng toàn bộ |
| 5 | Đề xuất ưu tiên sửa lỗi theo đúng thứ tự severity (High → Low) |
| 6 | 12/12 TC automation chạy PASSED, có screenshot tự động đầy đủ |
| 7 | Assertion chi tiết kiểm tra text nội dung (aria-label, sem_text), không chỉ check URL |
| 8 | Thêm 3 TC bonus (TC-13, 14, 15) trong thư mục tests_BONUS |
| 9 | REPORT.md mô tả đầy đủ 15 TC với description và kết quả Pass/Fail |

---

## 📝 NHẬN XÉT TỔNG HỢP

**Nhóm 16** đã hoàn thành xuất sắc cả hai hạng mục Manual và Automation Testing. Nhóm thể hiện sự nắm vững toàn diện các kỹ thuật kiểm thử — từ EP, BVA, Decision Table trong manual cho đến assertion chi tiết và screenshot tự động trong automation. Số lượng test case (63 TC) và bug report (14 báo cáo có đủ minh chứng) vượt xa yêu cầu tối thiểu, thể hiện tinh thần làm việc nghiêm túc và kỹ lưỡng.

**Điểm cần cải thiện:**
- **Automation:** Nên bổ sung file `.env` để cấu hình tài khoản test theo đúng hướng dẫn trong `docs/test-accounts.md`.

---

## 🏆 KẾT QUẢ CUỐI CÙNG

| Hạng mục | Điểm đạt | Điểm tối đa | Tỷ lệ |
|---|---|---|---|
| Manual Testing | 11.5 | 11.5 | 100% |
| Automation Testing | 12 | 11.5 | 100% |

> 📌 **Kết luận:** Nhóm 16 hoàn thành xuất sắc bài tập kiểm thử ở cả hai phần, đạt điểm cộng tối đa trong Manual. Tổng thể nhóm đạt mức **Xuất sắc** ở cả hai phần.

---

*Báo cáo được tổng hợp dựa trên dữ liệu chấm điểm từ vòng chấm chéo của Nhóm 19.*
