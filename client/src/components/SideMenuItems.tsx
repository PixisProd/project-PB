import React from "react";

interface SideMenuItemsProps {
    icon: React.ReactNode;
    label: string;
    collapsed: boolean;
    onClick: () => void;
}

const SideMenuItems: React.FC<SideMenuItemsProps> = ({icon, label, collapsed, onClick}) => {
    return (
        <button onClick={onClick} className="side-menu-button">
            {icon}
            <span className={`duration-300 origin-left transition whitespace-nowrap ${collapsed ? 'opacity-0 scale-x-0' : 'opacity-100 scale-x-100'}`}>
                {label}
            </span>
        </button>
    );
};

export default SideMenuItems