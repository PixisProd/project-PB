function Register() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-pbblack px-2.5">
      <div className="text-left flex flex-col w-full h-full max-h-[316] max-w-[366px]">
        <div>
          <h1 className="text-pbwhite font-bold text-2xl mb-">Create a PromptBox Account</h1>
          <p className="mb-[30px] text-pbwhite text-base">Hey there, already with us? <a href="/" className="transition hover:text-blue-600 text-bluelink">Log In</a></p>
        </div>
        <div className="flex flex-col">
          <label htmlFor="email" className="mb-2.5 text-pbwhite text-sm">
            Email
          </label>
          <input className="place-holder mb-5" id="email" type="text" placeholder="pixis@magic.com" />
        </div>
        <div className="flex flex-col">
          <label htmlFor="password" className="mb-2.5 text-pbwhite text-sm">
            Password
          </label>
          <input className="place-holder mb-7" id="password" type="password" placeholder="qwerty123" />
        </div>
        <button type="submit" className="white-button w-full">
          Continue
        </button>
      </div>
    </div>
  );
}

export default Register;
