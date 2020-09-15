class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    esporte = db.Column(db.Integer) 
    numero_jogadores = db.Column(db.String(254))
    def __str__(self):
        return self.nome + "," + self.esporte + "," + str(self.numero_jogadores) 
    
if __name__ == "__main__":
   db.create_all()
   nova = Time(nome = "Liquid", esporte = "E-sports", numero_jogadores = 5)
   db.session.add(nova)
   db.session.commit()  
   print(nova.nome)
   todas = db.session.query(Time).all()
   print(todas)
   for p in todas: print(p)