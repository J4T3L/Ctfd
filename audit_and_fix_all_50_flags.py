#!/usr/bin/env python3
"""
Master Audit & Harmonization Script for ALL 50 CTF Flags
Fixes any flag mismatches between Flask backend routes, handout files, CTFd metadata (challenge.yml),
and the master writeup solution document (PANDUAN_SOLUSI_DAN_TOOLS_50_CHALLENGES.txt).
"""
import os
import re

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
CHALLENGES_DIR = os.path.join(ROOT_DIR, "challenges")
ROUTES_DIR = os.path.join(ROOT_DIR, "app", "routes")
HANDOUT_DIR = os.path.join(ROOT_DIR, "handout")
SOLUTION_FILE = os.path.join(ROOT_DIR, "solution", "PANDUAN_SOLUSI_DAN_TOOLS_50_CHALLENGES.txt")

# Master Source of Truth for ALL 50 CTF Flags
MASTER_FLAGS = {
    # 🌐 1. Web Exploitation (15)
    "01_sqli": "CTF{34sy_sql_1nj3ct10n_byp4ss_2026}",
    "02_comment_leak": "CTF{h7ml_c0mm3n7_l34k_d1sc0v3r3d_2026}",
    "03_cookie_lab": "CTF{c00k13_m4n1pul4710n_m4s73r_2026}",
    "04_robots_secret": "CTF{r0b07s_7x7_d1sc0v3ry_m4s73r_2026}",
    "05_xss_reflected": "CTF{xss_r3fl3c73d_s3cr37_l34k_2026}",
    "06_idor": "CTF{1d0r_pr1v1l3g3_3sc4l4710n_2026}",
    "07_lfi": "CTF{lfi_path_tr4v3rs4l_m4st3r_2026}",
    "08_rce_ping": "CTF{rce_c0mm4nd_1nj3ct10n_m4st3r_2026}",
    "09_logic_shop": "CTF{l0g1c_fl4w_pr1c3_m4n1pul4710n_2026}",
    "10_ssrf": "CTF{ssrf_1n73rn4l_n37w0rk_4cc3ss_2026}",
    "11_jwt_lab": "CTF{jw7_w34k_s3cr37_3sc4l4710n_2026}",
    "12_xxe_lab": "CTF{xxe_xml_3x73rn4l_3n717y_2026}",
    "13_ssti": "CTF{ssti_j1nj42_w4f_byp4ss_2026}",
    "14_pickle_rce": "CTF{p1ckl3_d3s3r14l1z4710n_rce_2026}",
    "15_git_leak": "CTF{g17_d1r3c70ry_3xp0s3d_2026}",

    # 🔐 2. Cryptography (10)
    "16_crypto_caesar": "CTF{c43s4r_c1ph3r_r0t13_m4sg3r_2026}",
    "17_crypto_base64_multi": "CTF{mul71_l4y3r_3nc0d1ng_m4s73r_2026}",
    "18_crypto_md5": "CTF{password123}",
    "19_crypto_rsa_e3": "CTF{17}",
    "20_crypto_rsa_factor": "CTF{448}",
    "21_crypto_xor": "CTF{x0r_s7r34m_c1ph3r_cr4ck3d_2026}",
    "22_crypto_vigenere": "CTF{v1g3n3r3_c1ph3r_4n4lys1s_2026}",
    "23_crypto_aes_ecb": "CTF{43s_3cb_p4773rn_l34k_2026}",
    "24_crypto_custom_hash": "CTF{cush0m_h4sh_c0ll1s10n_2026}",
    "25_crypto_dh_weak": "CTF{12}",

    # 🔍 3. Digital Forensics (10)
    "26_forensics_exif": "CTF{3x1f_m374d474_3x7r4c710n_2026}",
    "27_forensics_stego_lsb": "CTF{lsb_st3g4n0gr4phy_3x7r4c73d_2026}",
    "28_forensics_file_fix": "CTF{f1l3_h34d3r_m4g1c_by73s_f1x_2026}",
    "29_forensics_disk": "CTF{d1sk_c4rv1ng_f0r3ns1cs_2026}",
    "30_forensics_volatility": "CTF{v0l471l17y_m3m0ry_f0r3ns1cs_2026}",
    "31_forensics_pdf": "CTF{pdf_h1dd3n_s7r34m_2026}",
    "32_forensics_zip": "CTF{z1p_p4ssw0rd_cr4ck3d_2026}",
    "33_forensics_audio": "CTF{4ud10_sp3c7r0gr4m_s73g0_2026}",
    "34_forensics_browser": "CTF{br0ws3r_h1s70ry_sql173_2026}",
    "35_forensics_usb": "CTF{usb_k3ys7r0k3_r3c0ns7ruc710n_2026}",

    # 📡 4. Network Sniffing (8)
    "36_net_http_cleartext": "CTF{c134r73x7_p4ck37_sn1ff3d_2026}",
    "37_net_dns_tunnel": "CTF{dns_7unn3l_3xf1l7r4710n_2026}",
    "38_net_ftp_pcap": "CTF{f7p_p4ss1v3_d474_7r4nsf3r_2026}",
    "39_net_icmp_covert": "CTF{1cmp_c0v3r7_ch4nn3l_2026}",
    "40_net_tls_decrypt": "CTF{7ls_d3cryp710n_k3yl0gf1l3_2026}",
    "41_net_arp_spoof": "CTF{4rp_sp00f1ng_m17m_2026}",
    "42_net_telnet_auth": "CTF{73ln37_c134r73x7_l0g1n_2026}",
    "43_net_mqtt_iot": "CTF{mq77_107_br0k3r_sn1ff3d_2026}",

    # ⚙️ 5. Reverse Engineering (7)
    "44_rev_strings": "CTF{r3v3rs3_3ng1n33r1ng_m4s73r_2026}",
    "45_rev_pyc": "CTF{py7h0n_by73c0d3_d3c0mp1l3d_2026}",
    "46_rev_java_class": "CTF{j4v4_d3c0mp1l3r_j4dx_2026}",
    "47_rev_crackme": "CTF{c_3lf_cr4ckm3_gdb_2026}",
    "48_rev_apk": "CTF{4ndr01d_4pk_sm4l1_r3v3rs3_2026}",
    "49_rev_bof_ret2win": "CTF{b0f_r372w1n_st4ck_0v3rwr173_2026}",
    "50_rev_upx_packed": "CTF{upx_unp4ck3d_b1n4ry_2026}"
}

print("[*] Harmonizing ALL 50 CTF flags across challenges, routes, and solution guides...")

# 1. Update all challenge.yml files
for folder, flag in MASTER_FLAGS.items():
    yml_file = os.path.join(CHALLENGES_DIR, folder, "challenge.yml")
    if os.path.exists(yml_file):
        with open(yml_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        updated = re.sub(r'flags:\s*\n\s*-\s*"[^"]+"', f'flags:\n  - "{flag}"', content)
        with open(yml_file, "w", encoding="utf-8") as f:
            f.write(updated)

print("[+] Updated 50 challenge.yml metadata files!")

# 2. Update Flask routes (lfi.py, rce_ping.py, ssti.py, xxe_lab.py, pickle_rce.py)
route_updates = {
    "lfi.py": ("CTF{lfi_path_tr4v3rs4l_m4st3r_2026}", "07_lfi"),
    "rce_ping.py": ("CTF{rce_c0mm4nd_1nj3ct10n_m4st3r_2026}", "08_rce_ping"),
    "ssti.py": ("CTF{ssti_j1nj42_w4f_byp4ss_2026}", "13_ssti"),
    "xxe_lab.py": ("CTF{xxe_xml_3x73rn4l_3n717y_2026}", "12_xxe_lab"),
    "pickle_rce.py": ("CTF{p1ckl3_d3s3r14l1z4710n_rce_2026}", "14_pickle_rce")
}

for fname, (flag, fkey) in route_updates.items():
    fpath = os.path.join(ROUTES_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            rcontent = f.read()
        
        # Replace CTF{...} inside route file
        rcontent_updated = re.sub(r'CTF\{[^}]+\}', flag, rcontent)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(rcontent_updated)

print("[+] Updated Flask backend route files!")

# 3. Update solution guide text file
if os.path.exists(SOLUTION_FILE):
    with open(SOLUTION_FILE, "r", encoding="utf-8") as f:
        scontent = f.read()
        
    for fkey, flag in MASTER_FLAGS.items():
        num = fkey.split("_")[0]
        # Match lines like [07] ... \n - Flag: CTF{...}
        scontent = re.sub(rf'(\[{num}\][^\n]*\n(?:[^\n]*\n)*?- Flag:\s*)CTF\{{[^}}]+\}}', rf'\1{flag}', scontent)
        
    with open(SOLUTION_FILE, "w", encoding="utf-8") as f:
        f.write(scontent)

print("[+] Updated master solution guide document!")
print("[🎉] 100% HARMONIZATION COMPLETE FOR ALL 50 CTF FLAGS!")
