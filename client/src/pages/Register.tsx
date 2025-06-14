import PasswordToggleIcon from '../components/PasswordToggleIcon';
import { useState } from 'react';

function Register() {
  const [showPassword, setShowPassword] = useState(false);

  const togglePassword = () => {
    setShowPassword((prev) => !prev)
  };


  return (
    <div className="min-h-screen flex items-center justify-center bg-pbblack px-2.5">
      <div className="text-left flex flex-col w-full h-full max-h-[316] max-w-[366px]">
        <div>
          <h1 className="text-pbwhite font-bold text-2xl mb-">Create a PromptBox Account</h1>
          <p className="mb-[30px] text-pbwhite text-base">Hey there, already with us? <a href="/" className="pb-link">Log In</a></p>
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
          <div className="relative">
            <input className="w-full place-holder mb-7" id="password" type={showPassword ? "text" : "password"} placeholder="••••••••••" />
            <button  className="absolute right-4 top-[19px] cursor-pointer -translate-y-1/2 hover:opacity-85 transition" onClick={togglePassword} type="button">
              <PasswordToggleIcon visible={showPassword}></PasswordToggleIcon>
            </button>
          </div>
        </div>
        <button type="submit" className="white-button w-full">
          Continue
        </button>
      </div>
    </div>
  );
}

export default Register;
