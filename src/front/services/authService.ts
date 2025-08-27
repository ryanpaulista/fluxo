const apiUrl = process.env.NEXT_PUBLIC_API_URL;

export const authService = {
    /**
     * Envia as credencias para o endpoint de login e retorna o token de acesso.
     * @param email Email do usuário
     * @param password Senha do usuário
     * @return os dados do usuário ou erro caso não consiga autenticar
     */
    async login(email: string, password: string): Promise<any> {
        
        const response = await fetch(`${apiUrl}/user/auth/`, {
            method: "POST",
            headers: {
                "Content-type": "application/json",
            },
            body: JSON.stringify({email, password}),
        });
        if (!response.ok){
            throw new Error("Login failed");
        }

        const data = await response.json();
        
        // Não é necessário mais salvar o tokens, o navegador faz isso
        return data; // Retorno da mensagem de sucesso
    },

    async logout(): Promise<void> {
        await fetch(`${apiUrl}/user/logout/`, {
            method: "POST",
            // Os cookies de autenticação são enviador automaticamente pelo navegador
        });
    },
};