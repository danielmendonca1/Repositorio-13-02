programa
{
	
	funcao inicio()
	{
		logico teste1, teste2, operacao_e, operacao_ou, operacao_nao, insanidade

		//ou = 1*
		//e = 2*
		//nao = 3*

		
		teste1 = falso
		teste2 = verdadeiro
		operacao_e = teste1 e teste2 //e = segunda falso, resto falso
		operacao_ou = teste1 ou teste2 //tudo verdadeiro
		operacao_nao = nao operacao_e // nao = tudo falso
		insanidade = operacao_ou e nao operacao_nao //ou = primeiro verdadeiro, resto verdadeiro
		escreva (insanidade)
		
	}
}
 		
