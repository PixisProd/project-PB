import { PlusIcon, WrenchScrewdriverIcon, ChevronLeftIcon, MagnifyingGlassIcon } from "@heroicons/react/24/outline"
import { useState, useEffect } from "react";
import SideMenuItems from "../components/SideMenuItems";
import PromptCard from "../components/PromptCard";

function Dashboard() {
    const [collapsed, setCollapsed] = useState(true);

    useEffect(() => {
        setCollapsed(false);
    }, [])

    return (
        <div className="h-screen w-screen flex bg-pbblack px-2.5 py-2.5">
            <aside className={`transition-all duration-600 p-3 flex flex-col bg-pbgray max-h-screen w-full ${!collapsed ? 'max-w-[300px]' : 'max-w-[74px]'} rounded-3xl border border-pbborder`}>
                <div className="flex items-center w-full mb-15">
                    <button onClick={() => setCollapsed(!collapsed)} className="transition text-pbwhite hover:text-pbgray ml-auto hover:bg-gray-300 rounded-3xl p-1">
                        <ChevronLeftIcon className={`pr-0.5 size-10 text-inherit transition-transform duration-600 ${collapsed ? 'rotate-180' : ''}`}/>
                    </button>
                </div>
                <nav className="text-pbwhite space-y-4">
                    <div className="flex items-center mb-2 px-3 h-5">
                        <WrenchScrewdriverIcon className="size-6 min-w-6 min-h-6"/>
                        <h2 className={`transition duration-300 origin-left ${collapsed ? 'scale-x-0 opacity-0' : 'scale-x-100 opacity-100'} font-bold text-2xl ml-3`}>Utils</h2>
                    </div>
                    <hr className="border-pbwhite brightness-75 rounded-2xl" />
                    <SideMenuItems icon={<PlusIcon className="size-6 min-w-6 min-h-6"/>} label="Add prompt" collapsed={collapsed} onClick={() => {}}/>
                </nav>
                <div className="flex border p-4 border-pbborder mt-auto h-12 w-full bg-pbblack rounded-3xl">
                    <p className="flex items-center text-pbwhite">Plan</p>
                </div>
            </aside>
            <main className=" w-full ml-3 mr-3 flex flex-col max-h-screen">
                <div className="animate-slide-up-fade relative">
                    <button className="hover:brightness-75 transition absolute left-3 top-[23px] -translate-y-1/2 cursor-pointer">
                        <MagnifyingGlassIcon className="size-6 text-pbwhite" />
                    </button>
                    <input className="text-2xl mb-3 w-full place-holder !pl-11" type="text" name="search" id="search" placeholder="Search"/>
                </div>
                <div className="flex flex-1 min-h-0 relative">
                    <div className="absolute top-0 left-0 right-0 z-10 h-4 bg-gradient-to-b from-pbblack to-transparent pointer-events-none" />
                    <div className="overflow-y-auto h-full">            
                        <div className={`transition grid ${!collapsed ? "grid-cols-3" : "grid-cols-4"} gap-2`}>
                            <PromptCard />
                            <PromptCard />
                            <PromptCard />
                            <PromptCard />
                            <PromptCard />
                            <PromptCard />
                            <PromptCard title="Product Desc for my dear company zakazchik n ful" use_case="sjdfkljasdhgjkhsadkjghadkjfhgjkdafhgjkdhfkjgadfkgj"></PromptCard>
                        </div>
                    </div>
                    <div className="absolute bottom-0 left-0 right-0 z-10 h-4 bg-gradient-to-t from-pbblack to-transparent pointer-events-none" />
                </div>
            </main>
            <aside className="ml-auto p-3 flex flex-col bg-pbgray max-h-screen w-full max-w-[258px] rounded-3xl border border-pbborder">
                
            </aside>
        </div>
    )
}

export default Dashboard