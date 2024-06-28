from pathlib import Path

home = Path(__file__).parent
rutaj = Path(home/'pinturas.json')
rutac = Path(home/'pinturas.csv')

menup = ['Ver listado de pinturas'
             'Buscar pinturas'
             'Agregar pintura'
             'Eliminar pintuar'
             'Exportar pinturas']
