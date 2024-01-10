class Tournament:
    def __init__(self):
        self.individuals = []
        self.teams = []
        self.events = {}

    def display_menu(self):
        print(f"----- Turnir Menyu -----")
        print("1. Shaxsiy bo'limga ro'yxatdan o'tish")
        print("2. Jamoaga ro'yxatdan o'tish")
        print("3. Faqat bitta hodisaga ro'yxatdan o'tish")
        print("4. Ro'yxatdan o'tgan qatnashchilarni ko'rish")
        print("5. Hodisa natijalarini yozish")
        print("6. Hodisa tartibini ko'rish")
        print("7. Chiqish")

    def register_individual(self):
        if len(self.individuals) >= 20:
            print("Kechirasiz, maksimal shaxsiy qatnashchilar soni tugagan.")
            return

        ism = input("Ismingizni kiriting: ")
        if not ism:
            print("Ism bo'sh bo'lishi mumkin emas.")
            return

        self.individuals.append({"name": ism, "events": {}})
        print(f"{ism} shaxsiy qatnashchisi sifatida ro'yxatdan o'tdi.")

    def register_team(self):
        if len(self.teams) >= 4:
            print("Kechirasiz, jamoalar maksimal soniga yetdi.")
            return

        jamoa_ismi = input("Jamoaning ismini kiriting: ")
        if not jamoa_ismi:
            print("Jamoaning nomi bo'sh bo'lishi mumkin emas.")
            return

        azolar = []
        for i in range(5):
            azo_ismi = input(f"{i + 1}-chi jamoa a'zosi ismini kiriting: ")
            if not azo_ismi:
                print("A'zo ismi bo'sh bo'lishi mumkin emas.")
                return
            azolar.append(azo_ismi)

        self.teams.append({"team_name": jamoa_ismi, "members": azolar, "events": {}})
        print(f"{jamoa_ismi} jamoasi sifatida ro'yxatdan o'tdi.")

    def register_one_event(self):
        ism = input("Ismingizni kiriting: ")
        if not ism:
            print("Ism bo'sh bo'lishi mumkin emas.")
            return

        hodisa_ismi = input("Ro'yxatdan o'tishni iste'fo qilgan hodisani ismini kiriting: ")
        if not hodisa_ismi:
            print("Hodisa nomi bo'sh bo'lishi mumkin emas.")
            return

        for shaxsiy in self.individuals:
            if shaxsiy["name"] == ism:
                shaxsiy["events"][hodisa_ismi] = 0
                print(f"{ism} {hodisa_ismi} hodisasi uchun ro'yxatdan o'tdi.")
                return

        for jamoa in self.teams:
            if jamoa["team_name"] == ism:
                jamoa["events"][hodisa_ismi] = 0
                print(f"{ism} {hodisa_ismi} hodisasi uchun ro'yxatdan o'tdi.")
                return

        print(f"{ism} nomli qatnashchi yoki jamoa topilmadi.")

    def record_event_results(self):
        hodisa_ismi = input("Hodisa nomini kiriting: ")
        if not hodisa_ismi:
            print("Hodisa nomi bo'sh bo'lishi mumkin emas.")
            return

        for i in range(1, 6):
            qatnashuvchi_ismi = input(f"{i}-chi qatnashuvchi yoki jamoa nomini kiriting: ")
            ballar = int(input(f"{qatnashuvchi_ismi} tomonidan olgan ballarni kiriting: "))

            for shaxsiy in self.individuals:
                if shaxsiy["name"] == qatnashuvchi_ismi and hodisa_ismi in shaxsiy["events"]:
                    shaxsiy["events"][hodisa_ismi] = ballar

            for jamoa in self.teams:
                if jamoa["team_name"] == qatnashuvchi_ismi and hodisa_ismi in jamoa["events"]:
                    jamoa["events"][hodisa_ismi] = ballar

    def view_event_standings(self):
        hodisa_ismi = input("Ko'rish uchun hodisa nomini kiriting: ")
        if not hodisa_ismi:
            print("Hodisa nomi bo'sh bo'lishi mumkin emas.")
            return

        tartib = []

        for shaxsiy in self.individuals:
            if hodisa_ismi in shaxsiy["events"]:
                tartib.append({"name": shaxsiy["name"], "ballar": shaxsiy["events"][hodisa_ismi]})

        for jamoa in self.teams:
            if hodisa_ismi in jamoa["events"]:
                umumiy_ballar = sum(jamoa["events"].values())
                tartib.append({"name": jamoa["team_name"], "ballar": umumiy_ballar})

        tartib.sort(key=lambda x: x["ballar"], reverse=True)

        print(f"----- {hodisa_ismi} hodisasi uchun tartib -----")
        for indeks, qatnashuvchi in enumerate(tartib, start=1):
            print(f"{indeks}. {qatnashuvchi['name']} - {qatnashuvchi['ballar']} ball")

    def view_registered_participants(self):
        print("----- Ro'yxatdan o'tgan qatnashchilar -----")
        print("Shaxsiylar:")
        for shaxsiy in self.individuals:
            print(shaxsiy["name"])
        print("Jamoalar:")
        for jamoa in self.teams:
            print(f"{jamoa['team_name']}: {', '.join(jamoa['members'])}")

    def run_tournament(self):
        while True:
            self.display_menu()
            tanlov = input("Tanlovni kiriting (1-7): ")

            if tanlov == "1":
                self.register_individual()
            elif tanlov == "2":
                self.register_team()
            elif tanlov == "3":
                self.register_one_event()
            elif tanlov == "4":
                self.view_registered_participants()
            elif tanlov == "5":
                self.record_event_results()
            elif tanlov == "6":
                self.view_event_standings()
            elif tanlov == "7":
                print("Turnirni tark etish...")
                break
            else:
                print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")


turnir = Tournament()
turnir.run_tournament()
