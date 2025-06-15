import PasswordToggleIcon from '../components/PasswordToggleIcon';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api/axios';


function Register() {
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      setError('')

      const regResponse = await api.post('/auth/registration', {
        email,
        password,
      });
      await api.post('/auth/login', {
        email,
        password,
      });
      console.log('Successful reg', regResponse.data)
      navigate('/about')
    } catch (err: any) {
      if (err.response) {
        setError(err.response.data.msg || err.response.data.detail[0].ctx.reason || 'Something went wrong');
      } else {
        setError('Network Error');
      }
    }
  };


  const togglePassword = () => {
    setShowPassword((prev) => !prev)
  };


  return (
    <div className="min-h-screen flex items-center justify-center bg-pbblack px-2.5">
      <form onSubmit={handleSubmit} className="animate-slide-up-fade text-left flex flex-col w-full h-full max-h-[316] max-w-[366px]">
        <div>
          <h1 className="text-pbwhite font-bold text-2xl mb-">Create a PromptBox Account</h1>
          <p className="mb-[30px] text-pbwhite text-base">Hey there, already with us? <Link to="/login" className='pb-link'>Log In</Link></p>
        </div>
        <div className="flex flex-col">
          <label htmlFor="email" className="mb-2.5 text-pbwhite text-sm">
            Email
          </label>
          <input value={email} onChange={(e) => setEmail(e.target.value)} className="place-holder mb-5" id="email" type="text" placeholder="pixis@magic.com" />
        </div>
        <div className="flex flex-col">
          <label htmlFor="password" className="mb-2.5 text-pbwhite text-sm">
            Password
          </label>
          <div className="relative">
            <input onChange={(e) => setPassword(e.target.value)} value={password} className="w-full place-holder mb-7" id="password" type={showPassword ? "text" : "password"} placeholder="••••••••••" />
            <button  className="absolute right-4 top-[19px] cursor-pointer -translate-y-1/2 hover:opacity-85 transition" onClick={togglePassword} type="button">
              <PasswordToggleIcon visible={showPassword}></PasswordToggleIcon>
            </button>
          </div>
        </div>

        {error && (
          <div className="text-red-500 mb-4">{error}</div>
        )}
        <button type="submit" className="white-button w-full">
          Create account
        </button>
      </form>
    </div>
  );
}

export default Register;
