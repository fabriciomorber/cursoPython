import pprint

filmDict = {
    "inception":{
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"],
    },
    "interstellar":{
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"],
    },
    "the dark knight":{
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"],
    },
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmDict)

# 1 - Buscar uma informação dentro de um dicionário aninhado
print(filmDict["interstellar"]["genre"])

# 2 - Adicionar novo item
filmDict["inception"]["director"] = "Christopher Nolan"
print(filmDict["inception"])

# 3 - Edxcluir um dicionário
del filmDict["the dark knight"]
print(filmDict)
