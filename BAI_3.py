product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

# print(product_list[0]["product_id"])

while True:
    choice = input("""

===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình\n
Nhập lựa chọn của bạn :  

""")
    match choice:
        case "1":
            # print(len(product_list))
            if len(product_list) == 0:
                print("Danh sách hiện đang trống")
            else:
                for product_id , product_info in enumerate(product_list , start= 1):
                    print(f"""{product_id} - {product_info['product_id']} | Tên : {product_info['product_name']}| Gía : {product_info['price']}| Số lượng : {product_info['quantity']}""")

        case "2":
            new_product_id = input("Nhập mã sản phẩm mới của bạn :  ").strip().upper()
            if new_product_id == "":
                print("Tên không được để trống")
                continue
            if any(product["product_id"] == new_product_id 
                   for product in product_list):
               print(f"{new_product_id} đã tồn tại trong danh sách!")
               continue
            new_product_name = input("Nhập tên sản phẩm mới của bạn :  ").strip().lower().capitalize()
            if new_product_name == "":
                print("Tên sản phẩm không được để trống")
                continue
           
            try:
                 new_product_price = int(input("Nhập giá của sản phẩm đó : "))
            except ValueError:
                print("Sai định dạng!")
                continue
            
            if new_product_price <= 0 :
                print("Giá của sản phẩm phải là một số lớn hơn 0!")
                continue
            
            try:
                product_new_quantity = int(input("Nhập số lượng sản phẩm đó : "))
            except ValueError:
                print("Sai định dạng!")
                continue

            if product_new_quantity <= 0:
                print("Số lượng sản phẩm phải là một con số lớn hơn 0!")
                continue

            new_product_info = {
                 "product_id": new_product_id,
                 "product_name" : new_product_name,
                 "price" : new_product_price,
                 "quantity" : product_new_quantity
            }
            product_list.append(new_product_info)
            print("Thêm sản phẩm thành công!")

        case "3":
                update_id_input = input("Nhập mã sản phẩm mà bạn muốn cập nhật").strip().upper()
                found = False

                for product in product_list:
                    if product["product_id"] == update_id_input:
                        found = True
                        print(f"\n--- Tìm thấy sản phẩm: {product['product_name']} ---")
                        
                        print(f"\n--- CẬP NHẬT SẢN PHẨM: {product['product_id']} ---")

                        new_name = input(f"Tên mới ({product['product_name']}): ").strip()

                        if new_name == "":
                            print("Không được để trống tên! ")
                        else:
                            #Lưu tên và tiến hành hỏi Giá
                            product["product_name"] = new_name.title()
                            
                            new_price = input(f"Giá mới ({product['price']}): ").strip()
                            if not new_price.isdigit() or int(new_price) <= 0:
                                print("Giá không hợp lệ! Hủy cập nhật.")
                            else:
                                # tiến hành hỏi Số lượng
                                product["price"] = int(new_price)
                                
                                new_quantity = input(f"Số lượng mới ({product['quantity']}): ").strip()
                                if not new_quantity.isdigit() or int(new_quantity) < 0:
                                    print("Số lượng không hợp lệ! Hủy cập nhật.")
                                else:
                                    #Lưu và hoàn tất
                                    product["quantity"] = int(new_quantity)
                                    print("\nCập nhật thành công toàn bộ thông tin!")
                                    break  

                                if not found:
                                    print("Không tìm thấy mã sản phẩm này trong hệ thống!")
        
        case "4":
            delete_product_input = input("Nhập mã sản phẩm mà bạn muốn xóa : ").strip().upper()
            found_product = False
            for product_id , product_info in enumerate(product_list , start=1):
                if product_info["product_id"] == delete_product_input:
                    product_list.remove(product_info)
                    found_product = True
                    break
            
            if found_product == False:
                print(f"Không tìm thấy sản phẩm có id {found_product}")

        case "5":
            print("Thoát chương trình,,,")
            break
        case _:
            print("Lựa chọn không hợp lệ")