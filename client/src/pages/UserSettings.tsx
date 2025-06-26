import {Cog6ToothIcon, EnvelopeIcon, BellIcon, KeyIcon, } from "@heroicons/react/24/outline";

export default function UserSettings() {


  return (

    <div className="h-screen w-screen flex bg-pbblack px-2.5 py-2.5 items-center justify-start">
      {/* сам сайдбар  */}
      <aside className="bg-pbgray w-[45vh] ml-2 w-left-100 h-[95vh] rounded-3xl border-[1px] border-pbborder">
        {/* тут аватарка  */}
        <div className="ml-6 mt-7 flex items-center gap-4 mb-10">
          <img className="w-13 h-13 rounded-full" src="https://i.pravatar.cc/100" alt="avatar" />
          <span className="text-white font-['Inter', 'sans-serif'] font-semibold -mt-5 text-lg">User Name</span>
        </div> 
        {/* тут ебаная линия */}
        <div className="px-4">
          <hr className="my-4 border-t border-pbborder border-2" />
        </div>
        {/* тут ебучие кнопки ака вкладки */}
        <div className="flex flex-col gap-3.5 items-center">
          <button className="group flex items-center gap-2 w-80 h-13 border bg-pbblack border-pbborder px-4 py-2 rounded-2xl text-pbwhite relative shadow-lg shadow-black/50 hover:bg-pbwhite hover:text-pbblack transition-colors duration-300">
            <Cog6ToothIcon className="w-6 h-6 text-pbwhite group-hover:text-pbblack duration-300" />
             <span className="absolute left-1/2 -translate-x-1/2 text-lg">General</span>
          </button>
          <button className="group flex items-center gap-2 w-80 h-13 border bg-pbblack border-pbborder px-4 py-2 rounded-2xl text-pbwhite relative shadow-lg shadow-black/50 hover:bg-pbwhite hover:text-pbblack transition-colors duration-300">
            <BellIcon className="w-6 h-6 text-white" />
            <span className="absolute left-1/2 -translate-x-1/2 text-lg">Notifications</span>
          </button>
          <button className="group flex items-center gap-2 w-80 h-13 border bg-pbblack border-pbborder px-4 py-2 rounded-2xl text-pbwhite relative shadow-lg shadow-black/50 hover:bg-pbwhite hover:text-pbblack transition-colors duration-300">
            <EnvelopeIcon className="w-6 h-6 text-white" />
            <span className="absolute left-1/2 -translate-x-1/2 text-lg">Email</span>
          </button>
          <button className="group flex items-center gap-2 w-80 h-13 border bg-pbblack border-pbborder px-4 py-2 rounded-2xl text-pbwhite relative shadow-lg shadow-black/50 hover:bg-pbwhite hover:text-pbblack transition-colors duration-300">
            <KeyIcon className="w-6 h-6 text-white" />
            <span className="absolute left-1/2 -translate-x-1/2 text-lg">Password</span>
          </button>
        </div>
      </aside>

      <main className="flex-1 flex justify-center items-center px-6 h-screen">
        <div className="w-full h-[95vh] bg-pbgray p-6 rounded-3xl shadow-lg border-[1px] border-pbborder">
        </div>
      </main>
    </div>

  );
}