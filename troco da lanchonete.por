programa
{
	funcao inicio()
	{
		real valor_lanche, valor_pago, troco
	
		//PADARIA BIJU//
	
		//valor:
	    escreva("Digite o valor do lanche da padaria: ")
	    leia(valor_lanche)
	
	     //eu mesmo paguei:
	    escreva("Digite o valor que que eu mesmo paguei, hipoteticamente: ")
	    leia(valor_pago)
	    se (valor_pago >= valor_lanche)
	    {
	        troco = valor_pago - valor_lanche
	        escreva("Troco: R$ ", troco, "\n")
	    }
	   	senao {escreva("valor insuficiente! eu ainda devo dinheiro!./n")
	   	
		}
   	}
}
