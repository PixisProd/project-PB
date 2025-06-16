function Dashboard() {
    return (
        <div className="h-screen w-screen flex bg-pbblack px-2.5 py-2.5">
            <aside className="p-5 flex flex-col bg-pbgray max-h-screen w-full max-w-[300px] rounded-3xl border border-pbborder">
                <div className="h-10 w-10 bg-amber-50 mb-15"/>
                <nav>
                    <ol className="space-y-3 text-pbwhite">
                        <li><button>Prefs</button></li>
                        <li><button>One more</button></li>
                        <li><button>Plan</button></li>
                        <li><button className="cursor-pointer">Add new prompt</button></li>
                    </ol>
                </nav>
                <p className="">Plan</p>
            </aside>
            <main className="max-w-max w-full ml-3 flex flex-col max-h-screen">
                <div className="relative">
                    <button className="hover:opacity-85 transition absolute left-3 top-[23px] -translate-y-1/2 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6 text-pbwhite">
                            <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </svg>
                    </button>
                    <input className="text-2xl mb-3 w-full place-holder !pl-11" type="text" name="search" id="search" placeholder="Search"/>
                </div>
                <div className="min-h-0 relative">
                    <div className="absolute top-0 left-0 right-0 z-10 h-6 bg-gradient-to-b from-pbblack to-transparent pointer-events-none" />
                    <div className="overflow-y-auto h-full">            
                        <div className="grid grid-cols-3 gap-3">
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                            <div className="temp-prompt-card"/>
                        </div>
                    </div>
                    <div className="absolute bottom-0 left-0 right-0 z-10 h-6 bg-gradient-to-t from-pbblack to-transparent pointer-events-none" />
                </div>
            </main>
        </div>
    )
}

export default Dashboard