import Image from "next/image"

export default function Header() {
    return (
        <header className="flex">
            <div>
                <Image
                    src="/next.svg"
                    alt="Logo"
                    width={50}
                    height={50}

                    className="w-30 h-12"
                />
            </div>
            <nav >
                <ul className="flex align-center p-10">
                    <li>
                        <a href="/">Home</a>
                    </li>
                    <li>
                        <a href="/blog">Blog</a>
                    </li>
                </ul>
            </nav>
            
        </header>
    )
}