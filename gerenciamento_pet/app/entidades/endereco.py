class Endereco():
    def __init__(self, rua, cidade, estado):
        self.__rua = rua
        self.__cidade = cidade
        self.__estado = estado



        @property
        def nome(self):
            return self.__nome
        @nome.setter
        def nome(self, nome):
            self.__nome = nome

        @property
        def email(self):
            return self.email
        @email.setter
        def nome(self, email):
            self.email = email

            @property
            def cpf(self):
                return self.cpf

            @cpf.setter
            def cpf(self, cpf):
                self.cpf = cpf

                @property
                def data_nascimento(self):
                    return self.data_nascimento

                @data_nascimento.setter
                def data_nascimento(self, data_nascimento):
                    self.data_nascimento = data_nascimento

        @property
        def profissao(self):
            return self.profissao

        @profissao.setter
        def profissao(self, profissao):
            self.profissao = profissao

        @property
        def endereco(self):
            return self.endereco

        @profissao.setter
        def endereco(self, endereco):
            self.endereco = endereco