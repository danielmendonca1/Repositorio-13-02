import tkinter as tk
root = tk.Tk()
root.title("Estrutura base")
root.geometry("500x350")

#frame esquerdo:
esquerdo = tk.Frame(root, bg="lightblue", width=120)
esquerdo.pack(side="left", fill="y")
tk.Label(esquerdo, text="Frame Esquerdo", bg="lightblue").pack(anchor="n")

#frame direito:
direito = tk.Frame(root)
direito.pack(side="left", fill="both", expand=True)

#parte superior direita:
topo = tk.Frame(direito, bg="lightgreen")
topo.pack(fill="both", expand=True)
tk.Label(topo, text="Frame Direito", bg="lightgreen").pack(anchor="n")

#parte inferior direita:
baixo = tk.Frame(direito, bg="yellow", height=80)
baixo.pack(fill="x")
baixo.pack_propagate(False)
tk.Label(baixo, text="Frame Inferior Direito", bg="yellow").pack(anchor="w")

root.mainloop()
