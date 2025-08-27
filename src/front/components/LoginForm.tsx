'use client'

import {useState} from 'react';
import {authService} from '@/services/authService'

export default function LoginForm(){;
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState<string | null>(null);
    const [isLogged, setIsLoggedIn] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        try {
            await authService.login(email, password);
            alert('Realizado com sucesso');
            window.location.href = '/';
        } catch(err) {
            setError(err instanceof Error ? err.message : "Ocorreu um erro desconhecido.");
        }
    };

    const handleLogout = () => {
        authService.logout();
        alert("Logout realizado com sucesso.")
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Login</h2>
            <div>
                <label htmlFor="email">Email:</label>
                <input 
                    type="email" 
                    id='email'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </div>
            <div>
                <label htmlFor="password">Password:</label>
                <input 
                    type="text" 
                    id='password'
                    value={password}
                    onChange={(e)=>setPassword(e.target.value)}
                    required
                />
            </div>
            {error && <p style={{color:'red'}}>{error}</p>}
            <button type="submit">Entrar</button>
        </form>
    );

}