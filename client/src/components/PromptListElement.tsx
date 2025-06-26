import React from "react"
import { useState } from "react"
import { DocumentDuplicateIcon, PencilSquareIcon, CheckCircleIcon } from "@heroicons/react/24/outline"


type CardProps = {
    title: string
    use_case: string
    model: string
    tags?: string[]
}


const PromptListElement: React.FC<CardProps> = ({title, use_case, model, tags=[]}) => {
    const [copied, setCopied] = useState(false)

    const handleCopy = async () => {
        await navigator.clipboard.writeText('KindaPrompt')
        setCopied(true)
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className="group text-pbwhite flex flex-col h-[200px] p-4 w-full mb-2 bg-pbgray border border-pbborder rounded-2xl hover:border-pbwhite transition">
            <h2 className="text-2xl font-semibold">{title}</h2>
            <p className="mt-4 text-pbwhite brightness-75">{use_case}</p>
            <div className="flex mt-auto gap-3">
                {tags.length > 0 && (
                    <div className="relative overflow-hidden mt-auto w-full">
                        <div className="flex gap-2 whitespace-nowrap">
                            {tags.map((tag, idx) => (
                                <span key={idx} className="font-extralight h-max bg-pbblack px-2 py-1 rounded-xl">
                                    #{tag}
                                </span>
                            ))}
                        </div>
                        <div className="ml-auto pointer-events-none absolute right-0 top-0 h-full w-12 bg-gradient-to-l from-pbgray to-transparent" />
                    </div>
                )}
                <div className="ml-auto flex gap-1.5 text-pbblack">
                    <button className="opacity-0 group-hover:opacity-100 transition flex items-center p-3 w-max h-max bg-pbwhite cursor-pointer text-pbblack hover:brightness-85 rounded-xl">
                        <PencilSquareIcon className="size-6"/>
                    </button>
                    <button onClick={handleCopy} className="relative opacity-0 group-hover:opacity-100 transition flex items-center p-3 w-max h-max bg-pbwhite cursor-pointer text-pbblack hover:brightness-85 rounded-xl">
                        <DocumentDuplicateIcon className={`absolute size-6 transition-opacity ${copied ? "opacity-0" : "opacity-100"}`} />
                        <CheckCircleIcon className={`absolute size-6 transition-opacity ${copied ? "opacity-100" : "opacity-0"}`} />
                        <CheckCircleIcon className="size-6 invisible" />
                    </button>
                </div>
            </div>
        </div>
    )
}

export default PromptListElement;