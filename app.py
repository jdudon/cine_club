from PySide2 import QtWidgets, QtCore
import movies

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.le_movie_title = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_remove = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.le_movie_title)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_remove)

    def setup_connections(self):
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_remove.clicked.connect(self.remove_movie)
        self.le_movie_title.returnPressed.connect(self.add_movie)

    def add_movie(self):
        # Récupérer le texte da,s le line edit
        # Créer une instance 'Movie'
        # Ajouter le film dans le fichier json
        # Ajouter le titre du film dans le list widget

        le_value = self.le_movie_title.text()
        if not le_value:
            return False
        
        movie = movies.Movie(title = le_value)

        result = movie.add_to_movies()
        if result:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.li_films.addItem(lw_item)
        self.le_movie_title.setText("")

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

    def populate_movies(self):
        movies_list = movies.get_movies()
        for movie in movies_list:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
