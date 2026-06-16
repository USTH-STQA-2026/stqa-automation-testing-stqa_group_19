# 📋 BÁO CÁO CHẤM CHÉO – NHÓM 19

> **Người chấm:** Nhóm sinh viên (chấm chéo)
> **Nhóm được chấm:** Nhóm 19
> **Thời gian:** 15/06/2026
> **Thang điểm:** 10 (có điểm cộng tối đa +1.5)

---

## 📊 KẾT QUẢ TỔNG QUAN

| Hạng mục | Điểm |
|---|---|
| Current Result (ghi nhận ban đầu) | 10/10 |
| **MANUAL – Final Result (TB 3 vòng)** | **11.42 / 10 (+1.42 điểm cộng)** |
| **AUTOMATION – Final Result (TB 3 vòng)** | **11.50 / 10 (+1.50 điểm cộng)** |

---

## 🖊️ PHẦN 1: MANUAL TESTING

### 1.1 Điểm Bắt Buộc (Minimum Requirements)

| STT | Tiêu chí | Điểm tối đa | Vòng 1 (T.Lương + Linh) | Vòng 2 (Q.Anh + H.Anh) | Vòng 3 (M. Châu + M.Lương) |
|---|---|---|---|---|---|
| 1 | Fork repo starter → tạo repo nhóm (Đặt tên: `stqa-manual-<tên-nhóm>`) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 2 | Viết ít nhất 20 test case (phủ đủ chức năng chính) | 2 | ✅ 2 | ✅ 2 | ✅ 2 |
| 3 | Áp dụng ít nhất 3 kỹ thuật thiết kế kiểm thử (EP, BVA, Decision Table) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 4 | Bao gồm happy path + negative + boundary | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 5 | Thực thi tất cả TC trên hệ thống (ghi nhận Pass/Fail + actual result) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 6 | Tạo bug report cho mỗi TC Fail (đầy đủ bước tái hiện, severity) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 7 | Viết báo cáo tổng hợp (summary: thống kê, đánh giá, đề xuất) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 8 | Điền thông tin nhóm trong README.md (Bảng Team Information) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 9 | Nộp bài qua link repo hoặc Pull Request | 1 | ✅ 1 | ✅ 1 | ✅ 1 |

### 1.2 Điểm Cộng (Bonus)

| Mã | Tiêu chí | Điểm tối đa | Vòng 1 | Vòng 2 | Vòng 3 |
|---|---|---|---|---|---|
| B1 | Viết ≥ 25 test case phủ tất cả 8 REQ | 0.5 | ✅ 0.5 | ✅ 0.5 | ⚠️ 0.25 |
| B2 | Thêm bảng Decision Table hoàn chỉnh cho chức năng Mượn sách | 0.5 | ❌ 0 | ❌ 0 | ❌ 0 |
| B3 | Mỗi bug report có ảnh chụp minh chứng | 0.5 | ✅ 0.5 | ✅ 0.5 | ✅ 0.5 |
| B4 | Tổng hợp có đề xuất ưu tiên sửa lỗi (High trước, Low sau) | 0.5 | ✅ 0.5 | ✅ 0.5 | ✅ 0.5 |

> ⚠️ **Lưu ý B2:** Cả 3 vòng chấm đều ghi nhận **chưa có Decision Table** cho chức năng Mượn sách → **0/0.5 điểm cộng B2**

### 1.3 Tổng Điểm Manual

| | Vòng 1 | Vòng 2 | Vòng 3 | **Trung bình** |
|---|---|---|---|---|
| **Tổng điểm** | 11.5 | 11.5 | 11.25 | **≈ 11.42** |

> ✅ Điểm cộng tối đa +1.5 (trên thang 10). Nhóm 19 đạt **+1.25 điểm cộng** phần Manual (do thiếu B2).

---

## 🤖 PHẦN 2: AUTOMATION TESTING

### 2.1 Điểm Bắt Buộc (Minimum Requirements)

| STT | Tiêu chí | Điểm tối đa | Vòng 1 | Vòng 2 | Vòng 3 |
|---|---|---|---|---|---|
| 1 | Fork repo starter → tạo repo nhóm (Đặt tên: `stqa-automation-<tên-nhóm>`) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 2 | Cấu hình `.env` với tài khoản test (xem `docs/test-accounts.md`) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 3 | Hoàn thành tất cả 12 test case (TC-01 → TC-12) | 2 | ✅ 2 | ✅ 2 | ✅ 2 |
| 4 | Tất cả test phải chạy được (pytest không lỗi cú pháp) – PASS hoặc FAIL đều tính | 2 | ✅ 2 | ✅ 2 | ✅ 2 |
| 5 | Mỗi test có screenshot tự động (lưu vào `screenshots/`) | 1 | ✅ 1 | ✅ 1 | ✅ 1 |
| 6 | Điền thông tin nhóm trong README.md (Bảng Team Information) | 2 | ✅ 2 | ✅ 2 | ✅ 2 |
| 7 | Nộp bài qua Pull Request hoặc link repo | 1 | ✅ 1 | ✅ 1 | ✅ 1 |

### 2.2 Điểm Cộng (Bonus)

| Mã | Tiêu chí | Điểm tối đa | Vòng 1 | Vòng 2 | Vòng 3 |
|---|---|---|---|---|---|
| B1 | Thêm ≥ 3 test case mới ngoài 12 TC cho sẵn | 0.5 | ❌ 0 | ❌ 0 | ❌ 0 |
| B2 | Viết data-driven test (parametrize nhiều bộ dữ liệu cho 1 kịch bản) | 0.5 | ✅ 0.5 | ✅ 0.5 | ✅ 0.5 |
| B3 | Thêm assertion chi tiết (kiểm tra text cụ thể, không chỉ kiểm tra URL) | 0.5 | ✅ 0.5 | ✅ 0.5 | ✅ 0.5 |
| B4 | Viết mô tả ngắn cho mỗi test trong REPORT.md | 0.5 | ✅ 0.5 | ✅ 0.5 | ✅ 0.5 |

> ⚠️ **Lưu ý B1:** Cả 3 vòng đều ghi nhận **chỉ thêm 2 test case** (yêu cầu ≥ 3) → **0/0.5 điểm cộng B1**

### 2.3 Tổng Điểm Automation

| | Vòng 1 | Vòng 2 | Vòng 3 | **Trung bình** |
|---|---|---|---|---|
| **Tổng điểm** | 11.5 | 11.5 | 11.5 | **11.50** |

> ✅ Nhóm 19 đạt **+1.5 điểm cộng tối đa** phần Automation.

---

## 📐 RUBRIC ĐÁNH GIÁ CHI TIẾT

### Rubric – Manual Testing

| Tiêu chí | Trọng số | Đánh giá | Mức đạt |
|---|---|---|---|
| **Độ phủ chức năng** | 25% | ≥ 20 TC, phủ đủ 8 REQ, có happy + negative + boundary | ✅ **Xuất sắc (9–10)** |
| **Kỹ thuật thiết kế** | 25% | Áp dụng EP + BVA (đúng), thiếu Decision Table cho mượn sách | ⚠️ **Tốt (7–8)** |
| **Chất lượng mô tả** | 20% | Bước đánh số rõ, dữ liệu cụ thể, expected result kiểm chứng được | ✅ **Xuất sắc (9–10)** |
| **Báo cáo lỗi** | 20% | Đầy đủ bước tái hiện, severity có giải thích, có minh chứng ảnh | ✅ **Xuất sắc (9–10)** |
| **Trình bày & format** | 10% | Đúng template, format rõ | ✅ **Xuất sắc (9–10)** |

### Rubric – Automation Testing

| Tiêu chí | Trọng số | Đánh giá | Mức đạt |
|---|---|---|---|
| **Hoàn thành TC** | 40% | 12/12 TC chạy được | ✅ **Xuất sắc (9–10)** |
| **Chất lượng code** | 25% | Assertion cụ thể (kiểm tra text, trạng thái), code sạch, có comment | ✅ **Xuất sắc (9–10)** |
| **Xử lý Flutter Web** | 15% | Dùng đúng helper, Smart Wait hợp lý | ✅ **Xuất sắc (9–10)** |
| **Screenshot & Evidence** | 10% | Mỗi TC có screenshot rõ ràng | ✅ **Xuất sắc (9–10)** |
| **Teamwork & Format** | 10% | Thông tin nhóm đầy đủ, commit history rõ ràng, README cập nhật | ✅ **Xuất sắc (9–10)** |

---

## 🐛 CÁC VẤN ĐỀ GHI NHẬN

### ❌ Điểm trừ / Chưa đạt

| # | Vấn đề | Ảnh hưởng | Phần |
|---|---|---|---|
| 1 | **Thiếu Decision Table** cho chức năng Mượn sách (B2 Manual) | Mất 0.5 điểm cộng | Manual |
| 2 | **Chỉ thêm 2 TC mới** thay vì ≥ 3 TC ngoài 12 TC cho sẵn (B1 Automation) | Mất 0.5 điểm cộng | Automation |

### ✅ Điểm mạnh nổi bật

| # | Điểm mạnh |
|---|---|
| 1 | Hoàn thành đầy đủ tất cả 12 TC automation, test chạy được không lỗi cú pháp |
| 2 | Bug report đầy đủ ảnh chụp minh chứng, severity có giải thích |
| 3 | Áp dụng data-driven testing (pytest parametrize) |
| 4 | Assertion chi tiết kiểm tra text cụ thể, không chỉ kiểm tra URL |
| 5 | Có REPORT.md với mô tả ngắn cho mỗi test case |
| 6 | Đề xuất ưu tiên sửa lỗi (High → Low) trong báo cáo tổng hợp |
| 7 | ≥ 25 TC manual phủ đủ chức năng (vòng 1 & 2) |

---

## 📝 NHẬN XÉT TỔNG HỢP

**Nhóm 19** đã hoàn thành tốt cả hai hạng mục Manual và Automation Testing với chất lượng tổng thể ở mức **Xuất sắc**. Nhóm nắm vững các kỹ thuật kiểm thử cơ bản (EP, BVA), biết áp dụng data-driven testing và viết assertion chi tiết trong automation.

**Điểm cần cải thiện:**
- **Manual:** Cần bổ sung bảng **Decision Table đầy đủ** cho chức năng Mượn sách (B2) – đây là kỹ thuật quan trọng giúp bao phủ các tổ hợp điều kiện phức tạp.
- **Automation:** Cần thêm ít nhất **1 test case mới** (hiện chỉ có 2/3 yêu cầu) để đạt điểm cộng B1.

---

## 🏆 KẾT QUẢ CUỐI CÙNG

| Hạng mục | Điểm đạt | Điểm tối đa | Tỷ lệ |
|---|---|---|---|
| Manual Testing | ≈ 11.42 | 11.5 | 99.3% |
| Automation Testing | 11.50 | 11.5 | 100% |

> 📌 **Kết luận:** Nhóm 19 hoàn thành xuất sắc bài tập kiểm thử, chỉ còn 2 điểm cộng chưa đạt do thiếu Decision Table (Manual) và chưa đủ số TC mới (Automation). Tổng thể nhóm đạt mức **Xuất sắc** ở cả hai phần.

---

*Báo cáo được tổng hợp dựa trên dữ liệu chấm điểm từ 3 vòng chấm chéo độc lập.*
