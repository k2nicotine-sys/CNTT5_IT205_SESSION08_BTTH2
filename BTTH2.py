shop_name = ""
description = ""
discount_codes = []

while True:

    print("===== MENU =====")
    print("1. Nhập dữ liệu sản phẩm")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá")
    print("4. Tìm kiếm và thay thế")
    print("5. Thoát")
    choice = input("Chọn chức năng: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    match choice:
        case "1":
            shop_name = input(
                "Nhập tên shop: "
            ).strip()
            if shop_name == "":
                print("Tên shop không được bỏ trống")
                continue
            product_name = input(
                "Nhập tên sản phẩm: "
            ).strip()
            description = input(
                "Nhập mô tả sản phẩm: "
            ).strip()
            if description == "":
                print(
                    "Mô tả sản phẩm không được rỗng"
                )
                continue
            category = input(
                "Nhập danh mục: "
            ).strip()
            keywords = input(
                "Nhập từ khóa: "
            )
            keyword_list = keywords.split(",")
            print("Tên shop:", shop_name)
            print(
                "Tên sản phẩm:",
                product_name.title()
            )
            print(
                "Độ dài mô tả:",
                len(description)
            )
            print(
                "Danh mục:",
                category.lower()
            )
            print(
                "Số lượng từ khóa:",
                len(keyword_list)
            )
            print(
                "Mô tả thường:",
                description.lower()
            )
            print(
                "Mô tả hoa:",
                description.upper()
            )

        case "2":
            shop = input(
                "Nhập tên shop: "
            ).strip()
            if shop == "":
                print("Tên shop không được bỏ trống")
            else:
                shop = shop.lower()
                shop = shop.replace(" ", "-")
                if not shop.startswith("shop-"):
                    shop = "shop-" + shop
                print(
                    "Tên shop chuẩn hóa:",
                    shop
                )

        case "3":
            code = input(
                "Nhập mã giảm giá: "
            ).strip()
            if code == "":
                print("Mã giảm giá không được rỗng")
            elif " " in code:
                print(
                    "Mã giảm giá không được chứa khoảng trắng"
                )
            elif len(code) < 6 or len(code) > 12:
                print(
                    "Mã giảm giá phải từ 6 đến 12 ký tự"
                )
            elif not code.isupper():
                print(
                    "Mã giảm giá phải viết hoa"
                )
            elif not code.isalnum():
                print(
                    "Mã giảm giá chỉ chứa chữ và số"
                )
            elif not code.startswith("SALE"):
                print(
                    "Mã phải bắt đầu bằng SALE"
                )
            else:
                print("Mã giảm giá hợp lệ")
                discount_codes.append(code)
                print(
                    "Danh sách mã:",
                    discount_codes
                )

        case "4":
            if description == "":
                print("Chưa có mô tả sản phẩm")
                continue
            old = input(
                "Từ khóa cần tìm: "
            )
            new = input(
                "Từ khóa thay thế: "
            )
            if old in description:
                print(
                    "Số lần xuất hiện:",
                    description.count(old)
                )
                print(
                    "Mô tả mới:"
                )
                print(
                    description.replace(old, new)
                )
            else:
                print(
                    "Không tìm thấy từ khóa"
                )
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Chọn từ 1 đến 5")