'use client'
const apiUrl = process.env.NEXT_PUBLIC_API_URL;

import { useEffect, useState } from "react";

interface User {
    id: number;
    first_name: string;
    last_name: string;
}

interface UserListProps {
    accessToken: string | null;
}

export default function UserList({accessToken}: UserListProps) {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(()=>{
        if(!accessToken){
            setLoading(false);
            setError("Token de acesso não fornecido");
            return;
        }
        async function fetchUsers(accessToken: string){
            try{
                const response = await fetch(`${apiUrl}/user/`,{
                    headers: {
                        'Authorization': `Bearer ${accessToken}`
                    },
                    credentials: 'include', // Diz ao navegador para enviar cookies em requisições cross-origin
                });

                if (response.status === 401) {
                    throw new Error('Não autorizado. Seu token pode ser inválido.');
                }

                if(!response.ok){
                    throw new Error('Falha ao buscar usuários');
                }

                const data: User[] = await response.json();
                setUsers(data);
            } catch(err){
                setError(err instanceof Error ? err.message : "Um erro ocorreu");
            } finally {
                setLoading(false);
            }
        }
        fetchUsers(accessToken);

    }, [accessToken]); // O arrayvazio faz com que isso só rode uma vez

    if(loading) return <p>Carregando usuários...</p>;
    if(error) return <p>Erro: {error}</p>

    return (
        <div>
            <ul>
                {users.map((user)=>(
                    <li key={user.id}>
                        {user.first_name} {user.last_name}
                    </li>
                ))}
            </ul>
        </div>
    );
}



