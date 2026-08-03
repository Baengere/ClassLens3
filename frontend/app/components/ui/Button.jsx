export default function Button({children, className="", ...props}){
    return(
        <button
            {...props} className={`rounded-xl bg-blue-600 px-5 py-3 font-medium text-white transition hover:bg-blue-700 ${className}`}
        >
            {children}
        </button>
    )
}