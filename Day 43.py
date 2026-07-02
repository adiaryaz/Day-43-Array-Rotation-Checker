def is_rotation(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        return "No proceed"
    if len(arr1) != len(arr2):
        return "No proceed"
    if len(arr1) == 0:
        return "No proceed"

    concatenated = arr1 + arr1 
    if any(arr2 == concatenated[i:i+len(arr1)] for i in range(len(arr1))):
        return sum(arr1)  

    return max(arr1)

if __name__ == "__main__":
    import ast

    while True:
        try:
            input1 = input("Masukkan array 1 (contoh: [1, 2, 3]) atau tekan Enter untuk keluar: ")
            
            if input1.strip() == '':
                print("Program dihentikan.")
                break
            arr1 = ast.literal_eval(input1)

            input2 = input("Masukkan array 2 (contoh: [3, 1, 2]): ")
            arr2 = ast.literal_eval(input2)

            result = is_rotation(arr1, arr2)
            print(f"Hasil: {result}\n")
            print("-" * 30) 
            
        except Exception as e:
            print(f"Terjadi kesalahan (Input tidak valid): {e}\n")