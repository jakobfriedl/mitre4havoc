#!/usr/bin/env python
# -*- Coding: UTF-8 -*-
# Author: Jakob Friedl
# Created on: Mon, 31. Oct. 2023
# Description: Havoc plugin to show MITRE ATT&CK tactics and techniques 

import havocui
import json
import os 

json_file = "/opt/Havoc/data/extensions/mitre4havoc/tactics.json"
tactics = []
infos = {}

def select_ttp(data): 
    
    info_panel = """<style>
        a {
            color: #6272a4;
        }
        .error {
            color: #ff5555;
        }
        .title {
            color: #8be9fd;
        }
        tr {
            background-color: #555766;
        }
        td > a {
            color: white; 
        }
    </style>"""

    try:
        t = infos[data]
    except:
        # Root element selected
        info_panel = info_panel + f"""
        <div class="content">
            <h1 class='title'>MITRE ATT&CK Enterprise Tactics</h1>
            <h3>Tactics</h3>
            <ul>
        """
        
        for tac in tactics: 
            info_panel = info_panel + f"""
                <li><a href={tac['link']}>{tac['id']}</a> {tac['tactic']}</li>
            """

        info_panel = info_panel + f"""
            </ul>
        </div>
        """
        tree.setPanel(info_panel)
        return

    if 'tactic' in t.keys():
        info_panel = info_panel + f"""
        <div class="content">
            <h1><a href={t['link']}>{t['id']}</a> {t['tactic']}</h1>
            <p>{t['description']}</p>
            <p>{t['long-description']}</p>

            <h3>Techniques</h3>
            <ul>
        """
        
        for tec in t['techniques']:
            info_panel = info_panel + f"""
                <li><a href={tec['link']}>{tec['id']}</a> {tec['technique']}</li>
            """

        info_panel = info_panel + f"""
            </ul>
        </div>
        """

    elif 'technique' in t.keys():
        info_panel = info_panel + f"""
        <div class="content">
            <h1><a href={t['link']}>{t['id']}</a> {t['technique']}</h1>
            <p>{t['description']}</p> 

            <h3>Sub-techniques</h3>
            <ul>
        """

        if len(t['sub-techniques']) <= 0: 
            info_panel = info_panel + f"""
            </ul>
            <p class='error'>This technique does not have sub-techniques.</p>
            """
        else: 
            for sub in t['sub-techniques']:
                info_panel = info_panel + f"""
                    <li><a href={sub['link']}>{sub['id']}</a> <b>{sub['sub-technique']}</b><br>
                        <span>{sub['description']}</span>
                    </li>
                """

        info_panel = info_panel + f"""
            </ul>
        
            <h3>Mitigations</h3>
            """
        
        if len(t['mitigations']) <= 0:
            info_panel = info_panel + f"""
                </ul>
                <p class='error'>This technique does not have mitigations.</p>
            </div>
            """
        else:
            info_panel = info_panel + f"""
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Mitigation</th>
                        <th>Description</th>
                    </tr>
            """

            for mit in t['mitigations']:
                info_panel = info_panel + f"""
                    <tr>
                        <td><a href={mit['link']}>{mit['id']}</li></td>
                        <td>{mit['mitigation']}</td>
                        <td>{mit['description']}</td>
                    </tr>
                """

            info_panel = info_panel + f"""
                </table>
            </div>
            """
        
    tree.setPanel(info_panel)

tree = havocui.Tree("MITRE Enterprise TTPs", select_ttp, True)

def open_view():
    global tactics

    if not os.path.exists(json_file):
        havocui.messagebox("Error", f"{json_file} not found. Run python3 parse_mitre.py to create it or use the one provided in the mitre4havoc repository.")
    
    with open(json_file, "r") as f: 
        tactics = json.load(f)  
    
    for tac in tactics: 
        tac_l = f"{tac['id']}: {tac['tactic']}"
        infos[tac_l] = tac

        labels = []
        for tec in tac['techniques']:
            tec_l = f"{tec['id']}: {tec['technique']}"
            labels.append(tec_l)
            infos[tec_l] = tec

        tree.addRow(tac_l, *labels)

    tree.setBottomTab()

havocui.createtab("MITRE", "Open view", open_view)
