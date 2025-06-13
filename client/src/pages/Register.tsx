function Register() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-pbblack px-2.5">
      <div className="text-left flex flex-col w-full h-full max-h-[316] max-w-[366px]">
        <div>
          <h1 className="text-pbwhite font-bold text-2xl mb-">Create a PromptBox Account</h1>
          <p className="mb-[30px] text-pbwhite text-base">Hey there, already with us? <a href="/" className="transition hover:text-blue-600 text-bluelink">Log In</a></p>
        </div>
        <div>
          <label htmlFor="email" className="mb-[10px] text-pbwhite text-sm flex flex-col">
            Email
          </label>
          <input className="focus:border-white transition duration-300 focus:outline-none mb-[20px] text-pbwhite w-full max-w-[366px] max-y-[40px] border border-[#2C2C35] rounded-2xl px-5 py-1.5 placeholder:text-phtext bg-pbgray" id="email" type="text" placeholder="pixis@magic.com" />
        </div>
        <div>
          <label htmlFor="password" className="mb-[10px] text-pbwhite text-sm flex flex-col">
            Password
          </label>
          <input className="focus:border-white transition duration-300 focus:outline-none mb-[20px] text-pbwhite w-full max-w-[366px] max-y-[40px] border border-[#2C2C35] rounded-2xl px-5 py-1.5 placeholder:text-phtext bg-pbgray" id="password" type="password" placeholder="qwerty123" />
        </div>
        <button type="submit" className="cursor-pointer hover:bg-gray-300 transition bg-pbwhite rounded-xl px-2.5 py-2.5 w-full mx-auto max-w-[366px] max-h-[50px] block">
          Continue
        </button>
      </div>
    </div>
  );
}

export default Register;
