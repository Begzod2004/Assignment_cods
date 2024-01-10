class RestoranBandlikTakliflashTizimi:
    def __init__(self):
        self.bandliklar = {}

    def menyuni_korsatish(self):
        print("\nRestoran stoli bandligi takliflash tizimi")
        print("1. Bandlik tanlash")
        print("2. Bandlikni yangilash")
        print("3. Bandlikni bekor qilish")
        print("4. Bandliklarni ko'rish")
        print("5. Chiqish")

    def bandlik_tanlash(self):
        ism = input("Mijozning ismini kiriting: ")
        sanasi = input("Bandlik sanasini kiriting (YYYY-MM-DD): ")
        vaqti = input("Bandlik vaqtini kiriting (HH:MM): ")
        odamlar_soni = input("Odamlar sonini kiriting: ")
        kalit = (sanasi, vaqti)
        if kalit in self.bandliklar:
            print("Bu vaqtda bandlik allaqachon mavjud. Iltimos, boshqa vaqtni tanlang.")
        else:
            self.bandliklar[kalit] = (ism, odamlar_soni)
            print(f"{ism} uchun {sanasi} kuni, {vaqti} vaqtida, {odamlar_soni} kishi uchun bandlik olinadi.")

    def bandlikni_yangilash(self):
        sanasi = input("Bandlik sanasini yangilash (YYYY-MM-DD) uchun kiriting: ")
        vaqti = input("Bandlik vaqtini yangilash (HH:MM) uchun kiriting: ")
        kalit = (sanasi, vaqti)
        if kalit not in self.bandliklar:
            print("Bandlik topilmadi.")
        else:
            yangi_sana = input("Yangi bandlik sanasini kiriting (YYYY-MM-DD): ")
            yangi_vaqt = input("Yangi bandlik vaqtini kiriting (HH:MM): ")
            yangi_kalit = (yangi_sana, yangi_vaqt)
            if yangi_kalit in self.bandliklar:
                print("Bu vaqtda bandlik allaqachon mavjud. Iltimos, boshqa vaqtni tanlang.")
            else:
                self.bandliklar[yangi_kalit] = self.bandliklar.pop(kalit)
                print(f"Bandlik {yangi_sana} sanasiga, {yangi_vaqt} vaqtiga yangilandi.")

    def bandlikni_bekor_qilish(self):
        sanasi = input("Bekor qilish uchun bandlik sanasini kiriting (YYYY-MM-DD): ")
        vaqti = input("Bekor qilish uchun bandlik vaqtini kiriting (HH:MM): ")
        kalit = (sanasi, vaqti)
        if kalit not in self.bandliklar:
            print("Bandlik topilmadi.")
        else:
            del self.bandliklar[kalit]
            print("Bandlik bekor qilindi.")

    def bandliklarni_korish(self):
        if not self.bandliklar:
            print("Hech qanday bandlik topilmadi.")
        else:
            print("\nJoriy Bandliklar:")
            for (sanasi, vaqti), (ism, odamlar_soni) in self.bandliklar.items():
                print(f"Sana: {sanasi}, Vaqt: {vaqti}, Ism: {ism}, Odamlar: {odamlar_soni}")


def asosiy():
    tizim = RestoranBandlikTakliflashTizimi()
    while True:
        tizim.menyuni_korsatish()
        tanlov = input("Variantni tanlang: ")

        if tanlov == "1":
            tizim.bandlik_tanlash()
        elif tanlov == "2":
            tizim.bandlikni_yangilash()
        elif tanlov == "3":
            tizim.bandlikni_bekor_qilish()
        elif tanlov == "4":
            tizim.bandliklarni_korish()
        elif tanlov == "5":
            print("Tizimdan chiqish. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")


if __name__ == "__main__":
    asosiy()
