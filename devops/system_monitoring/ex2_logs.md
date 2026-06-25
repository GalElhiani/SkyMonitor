Jun 24 00:08:25 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 00:08:25 galelhiani systemd[1]: Starting Daily dpkg database backup service...
Jun 24 00:08:25 galelhiani systemd[1]: Starting Rotate log files...
Jun 24 00:08:25 galelhiani systemd[1]: dpkg-db-backup.service: Deactivated successfully.
Jun 24 00:08:25 galelhiani systemd[1]: Finished Daily dpkg database backup service.
Jun 24 00:08:25 galelhiani systemd[1]: Stopping Make remote CUPS printers available locally...
Jun 24 00:08:25 galelhiani systemd[1]: cups-browsed.service: Deactivated successfully.
Jun 24 00:08:25 galelhiani systemd[1]: Stopped Make remote CUPS printers available locally.
Jun 24 00:08:25 galelhiani systemd[1]: Stopping CUPS Scheduler...
Jun 24 00:08:25 galelhiani systemd[1]: cups.service: Deactivated successfully.
Jun 24 00:08:25 galelhiani systemd[1]: Stopped CUPS Scheduler.
Jun 24 00:08:25 galelhiani systemd[1]: cups.path: Deactivated successfully.
Jun 24 00:08:25 galelhiani systemd[1]: Stopped CUPS Scheduler.
Jun 24 00:08:25 galelhiani systemd[1]: Stopping CUPS Scheduler...
Jun 24 00:08:25 galelhiani systemd[1]: Started CUPS Scheduler.
Jun 24 00:08:25 galelhiani systemd[1]: cups.socket: Deactivated successfully.
Jun 24 00:08:25 galelhiani systemd[1]: Closed CUPS Scheduler.
Jun 24 00:08:25 galelhiani systemd[1]: Stopping CUPS Scheduler...
Jun 24 00:08:25 galelhiani systemd[1]: Listening on CUPS Scheduler.
Jun 24 00:08:25 galelhiani systemd[1]: Starting CUPS Scheduler...
Jun 24 00:08:25 galelhiani audit[4000]: AVC apparmor="DENIED" operation="capable" profile="/usr/sbin/cupsd" pid=4000 comm="cupsd" capability=12  capname="net_admin"
Jun 24 00:08:25 galelhiani systemd[1]: Started CUPS Scheduler.
Jun 24 00:08:25 galelhiani systemd[1]: Started Make remote CUPS printers available locally.
Jun 24 00:08:25 galelhiani kernel: audit: type=1400 audit(1782259705.613:75): apparmor="DENIED" operation="capable" profile="/usr/sbin/cupsd" pid=4000 comm="cupsd" capability=12  capname="net_admin"
Jun 24 00:08:25 galelhiani systemd[1]: logrotate.service: Deactivated successfully.
Jun 24 00:08:25 galelhiani systemd[1]: Finished Rotate log files.
Jun 24 00:41:09 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 00:41:09 galelhiani systemd[1]: Starting Daily man-db regeneration...
Jun 24 00:41:09 galelhiani systemd[1]: man-db.service: Deactivated successfully.
Jun 24 00:41:09 galelhiani systemd[1]: Finished Daily man-db regeneration.
Jun 24 00:58:34 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 01:15:51 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 01:31:32 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 02:06:08 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 02:37:21 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 02:56:52 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 02:56:52 galelhiani systemd[1]: Starting Message of the Day...
Jun 24 02:56:52 galelhiani 50-motd-news[4051]:  * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
Jun 24 02:56:52 galelhiani 50-motd-news[4051]:    just raised the bar for easy, resilient and secure K8s cluster deployment.
Jun 24 02:56:52 galelhiani 50-motd-news[4051]:    https://ubuntu.com/engage/secure-kubernetes-at-the-edge
Jun 24 02:56:52 galelhiani systemd[1]: motd-news.service: Deactivated successfully.
Jun 24 02:56:52 galelhiani systemd[1]: Finished Message of the Day.
Jun 24 03:13:48 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 03:14:25 galelhiani CRON[4059]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 03:14:25 galelhiani CRON[4060]: (root) CMD (test -e /run/systemd/system || SERVICE_MODE=1 /sbin/e2scrub_all -A -r)
Jun 24 03:14:25 galelhiani CRON[4059]: pam_unix(cron:session): session closed for user root
Jun 24 03:30:55 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 03:47:20 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 03:51:13 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 03:55:19 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 03:56:36 galelhiani systemd-timesyncd[792]: Timed out waiting for reply from 185.125.190.58:123 (ntp.ubuntu.com).
Jun 24 05:01:44 galelhiani systemd-timesyncd[792]: Initial synchronization to time server 185.125.190.57:123 (ntp.ubuntu.com).
Jun 24 05:01:44 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 05:05:08 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.75' (uid=1000 pid=1575 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 05:05:08 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 05:05:08 galelhiani dbus-daemon[857]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 05:05:08 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 05:05:08 galelhiani gnome-shell[1575]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 05:05:12 galelhiani gdm-password][4075]: gkr-pam: unlocked login keyring
Jun 24 05:05:12 galelhiani NetworkManager[858]: <info>  [1782277512.8769] agent-manager: agent[ebca55994d94eb2f,:1.75/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 05:05:12 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for software-update-available
Jun 24 05:05:12 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for livepatch
Jun 24 05:05:13 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.ArchiveManager1' requested by ':1.122' (uid=1000 pid=4080 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 05:05:13 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 05:05:13 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 05:05:13 galelhiani gnome-shell[1575]: DING: Detected async api for thumbnails
Jun 24 05:05:13 galelhiani gnome-shell[1575]: DING: GNOME nautilus 42.6
Jun 24 05:05:38 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 05:06:44 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:06:44 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:07:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:07:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:17:01 galelhiani CRON[4152]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 05:17:01 galelhiani CRON[4153]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 05:17:01 galelhiani CRON[4152]: pam_unix(cron:session): session closed for user root
Jun 24 05:18:28 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 05:18:28 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 05:28:37 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.75' (uid=1000 pid=1575 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 05:28:37 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 05:28:37 galelhiani dbus-daemon[857]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 05:28:37 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 05:28:37 galelhiani gnome-shell[1575]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 05:28:37 galelhiani gnome-shell[1575]: Object Gdm.UserVerifierProxy (0xaaaaf792c340), has been already disposed — impossible to access it. This might be caused by the object having been destroyed from C code using something such as destroy(), dispose(), or remove() vfuncs.
Jun 24 05:28:37 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 05:28:37 galelhiani gnome-shell[1575]: #0   aaaaf40597b8 i   resource:///org/gnome/gjs/modules/core/overrides/Gio.js:425 (3326fb3cdec0 @ 77)
Jun 24 05:28:37 galelhiani gnome-shell[1575]: JS ERROR: Failed to open reauthentication channel: Gio.IOErrorEnum: Error receiving data: Connection reset by peer
                                              _promisify/proto[asyncFunc]/</<@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:425:45
                                              ### Promise created here: ###
                                              _openReauthenticationChannel@resource:///org/gnome/shell/gdm/util.js:503:53
                                              begin@resource:///org/gnome/shell/gdm/util.js:254:18
                                              begin@resource:///org/gnome/shell/gdm/authPrompt.js:675:28
                                              _onReset@resource:///org/gnome/shell/ui/unlockDialog.js:784:26
                                              reset@resource:///org/gnome/shell/gdm/authPrompt.js:652:14
                                              _ensureAuthPrompt@resource:///org/gnome/shell/ui/unlockDialog.js:694:26
                                              _showPrompt@resource:///org/gnome/shell/ui/unlockDialog.js:725:14
                                              _init/<@resource:///org/gnome/shell/ui/unlockDialog.js:511:22
Jun 24 05:28:40 galelhiani gdm-password][4194]: gkr-pam: unlocked login keyring
Jun 24 05:28:40 galelhiani NetworkManager[858]: <info>  [1782278920.8686] agent-manager: agent[e96510fc58854bbc,:1.75/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 05:28:40 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for software-update-available
Jun 24 05:28:40 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for livepatch
Jun 24 05:28:40 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.ArchiveManager1' requested by ':1.127' (uid=1000 pid=4198 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 05:28:41 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 05:28:41 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 05:28:41 galelhiani gnome-shell[1575]: DING: Detected async api for thumbnails
Jun 24 05:28:41 galelhiani gnome-shell[1575]: DING: GNOME nautilus 42.6
Jun 24 05:29:07 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 05:29:42 galelhiani sudo[4270]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani ; USER=root ; COMMAND=/usr/bin/apt install samba
Jun 24 05:29:42 galelhiani sudo[4270]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 05:29:51 galelhiani groupadd[4580]: group added to /etc/group: name=rdma, GID=138
Jun 24 05:29:51 galelhiani groupadd[4580]: group added to /etc/gshadow: name=rdma
Jun 24 05:29:51 galelhiani groupadd[4580]: new group: name=rdma, GID=138
Jun 24 05:29:53 galelhiani groupadd[4779]: group added to /etc/group: name=sambashare, GID=139
Jun 24 05:29:53 galelhiani groupadd[4779]: group added to /etc/gshadow: name=sambashare
Jun 24 05:29:53 galelhiani groupadd[4779]: new group: name=sambashare, GID=139
Jun 24 05:29:53 galelhiani systemd[1]: Reloading.
Jun 24 05:29:53 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:53 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:53 galelhiani systemd[1]: Reloading.
Jun 24 05:29:53 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:53 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:54 galelhiani systemd[1]: Reloading.
Jun 24 05:29:54 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:54 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:54 galelhiani systemd[1]: Reloading.
Jun 24 05:29:54 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:54 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:54 galelhiani systemd[1]: Reloading.
Jun 24 05:29:54 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:54 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:54 galelhiani systemd[1]: Reloading.
Jun 24 05:29:54 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:54 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:54 galelhiani systemd[1]: Reloading.
Jun 24 05:29:54 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:29:54 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:29:54 galelhiani systemd[1]: Starting Samba NMB Daemon...
Jun 24 05:29:54 galelhiani systemd[1]: Started Samba NMB Daemon.
Jun 24 05:29:54 galelhiani systemd[1]: Starting Samba SMB Daemon...
Jun 24 05:29:54 galelhiani update-apparmor-samba-profile[5120]: grep: /etc/apparmor.d/samba/smbd-shares: No such file or directory
Jun 24 05:29:54 galelhiani update-apparmor-samba-profile[5123]: diff: /etc/apparmor.d/samba/smbd-shares: No such file or directory
Jun 24 05:29:54 galelhiani systemd[1]: Started Samba SMB Daemon.
Jun 24 05:29:57 galelhiani sudo[4270]: pam_unix(sudo:session): session closed for user root
Jun 24 05:32:32 galelhiani pkexec[5300]: pam_unix(polkit-1:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 05:32:32 galelhiani pkexec[5300]: galelhiani: Executing command [USER=root] [TTY=unknown] [CWD=/home/galelhiani] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Jun 24 05:35:21 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:35:21 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:35:31 galelhiani polkitd(authority=local)[869]: Registered Authentication Agent for unix-process:5327:5969146 (system bus name :1.149 [/usr/bin/pkttyagent --notify-fd 5 --fallback], object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Jun 24 05:35:37 galelhiani polkitd(authority=local)[869]: Operator of unix-session:2 successfully authenticated as unix-user:galelhiani to gain TEMPORARY authorization for action org.freedesktop.systemd1.manage-unit-files for system-bus-name::1.150 [systemctl enable --now smb] (owned by unix-user:galelhiani)
Jun 24 05:35:37 galelhiani polkitd(authority=local)[869]: Unregistered Authentication Agent for unix-process:5327:5969146 (system bus name :1.149, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
Jun 24 05:36:24 galelhiani gnome-shell[1575]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 22ms, your system is too slow
Jun 24 05:36:28 galelhiani polkitd(authority=local)[869]: Registered Authentication Agent for unix-process:5346:5974892 (system bus name :1.152 [/usr/bin/pkttyagent --notify-fd 5 --fallback], object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Jun 24 05:36:30 galelhiani polkitd(authority=local)[869]: Operator of unix-session:2 successfully authenticated as unix-user:galelhiani to gain TEMPORARY authorization for action org.freedesktop.systemd1.reload-daemon for system-bus-name::1.153 [systemctl daemon-reload] (owned by unix-user:galelhiani)
Jun 24 05:36:30 galelhiani systemd[1]: Reloading.
Jun 24 05:36:30 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:36:30 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:36:30 galelhiani polkitd(authority=local)[869]: Unregistered Authentication Agent for unix-process:5346:5974892 (system bus name :1.152, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
Jun 24 05:36:30 galelhiani polkitd(authority=local)[869]: Registered Authentication Agent for unix-process:5390:5975123 (system bus name :1.155 [/usr/bin/pkttyagent --notify-fd 5 --fallback], object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Jun 24 05:36:34 galelhiani polkitd(authority=local)[869]: Operator of unix-session:2 successfully authenticated as unix-user:galelhiani to gain TEMPORARY authorization for action org.freedesktop.systemd1.reload-daemon for system-bus-name::1.156 [systemctl daemon-reload] (owned by unix-user:galelhiani)
Jun 24 05:36:34 galelhiani systemd[1]: Reloading.
Jun 24 05:36:34 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:36:34 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:36:34 galelhiani polkitd(authority=local)[869]: Unregistered Authentication Agent for unix-process:5390:5975123 (system bus name :1.155, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
Jun 24 05:36:34 galelhiani polkitd(authority=local)[869]: Registered Authentication Agent for unix-process:5342:5974891 (system bus name :1.158 [/usr/bin/pkttyagent --notify-fd 5 --fallback], object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Jun 24 05:36:39 galelhiani polkitd(authority=local)[869]: Operator of unix-session:2 successfully authenticated as unix-user:galelhiani to gain TEMPORARY authorization for action org.freedesktop.systemd1.manage-unit-files for system-bus-name::1.159 [systemctl enable --now smbd] (owned by unix-user:galelhiani)
Jun 24 05:36:39 galelhiani systemd[1]: Reloading.
Jun 24 05:36:39 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 05:36:39 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 05:36:39 galelhiani polkitd(authority=local)[869]: Unregistered Authentication Agent for unix-process:5342:5974891 (system bus name :1.158, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
Jun 24 05:37:46 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:37:46 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:38:10 galelhiani gnome-shell[1575]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 22ms, your system is too slow
Jun 24 05:38:11 galelhiani gnome-shell[1575]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 25ms, your system is too slow
Jun 24 05:38:22 galelhiani gnome-shell[1575]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 36ms, your system is too slow
Jun 24 05:39:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:39:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:39:56 galelhiani systemd[1462]: Started VTE child process 5480 launched by gnome-terminal-server process 2335.
Jun 24 05:40:13 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.89' (uid=1000 pid=1948 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 24 05:40:13 galelhiani systemd[1462]: Starting Tracker metadata extractor...
Jun 24 05:40:13 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.freedesktop.Tracker3.Miner.Extract'
Jun 24 05:40:13 galelhiani systemd[1462]: Started Tracker metadata extractor.
Jun 24 05:40:21 galelhiani gnome-shell[1575]: DING: (gjs:4198): Gdk-WARNING **: 05:40:21.651: Tried to map a popup with a non-top most parent
Jun 24 05:40:24 galelhiani systemd[1462]: Started VTE child process 5507 launched by gnome-terminal-server process 2335.
Jun 24 05:40:29 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:40:29 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:41:48 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:41:48 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:42:18 galelhiani sudo[5527]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop ; USER=root ; COMMAND=/usr/bin/nano /etc/samba/smb.conf
Jun 24 05:42:18 galelhiani sudo[5527]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 05:42:37 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:42:37 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:42:55 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.106' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 05:42:55 galelhiani systemd[1]: Starting Hostname Service...
Jun 24 05:42:55 galelhiani dbus-daemon[857]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 24 05:42:55 galelhiani systemd[1]: Started Hostname Service.
Jun 24 05:42:57 galelhiani systemd[1462]: Started VTE child process 5536 launched by gnome-terminal-server process 2335.
Jun 24 05:43:09 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:43:09 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:43:25 galelhiani systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 24 05:43:30 galelhiani sudo[5527]: pam_unix(sudo:session): session closed for user root
Jun 24 05:44:53 galelhiani gnome-shell[1575]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 31ms, your system is too slow
Jun 24 05:44:53 galelhiani gnome-shell[1575]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: WARNING: log rate limit exceeded (5 msgs per 60min). Discarding future messages.
Jun 24 05:45:48 galelhiani sudo[5563]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop ; USER=root ; COMMAND=/usr/bin/smbpasswd -a galelhiani
Jun 24 05:45:48 galelhiani sudo[5563]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 05:45:55 galelhiani sudo[5563]: pam_unix(sudo:session): session closed for user root
Jun 24 05:46:11 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:46:11 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:46:14 galelhiani sudo[5568]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop ; USER=root ; COMMAND=/usr/bin/systemctl restart smb nmb
Jun 24 05:46:14 galelhiani sudo[5568]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 05:46:14 galelhiani sudo[5568]: pam_unix(sudo:session): session closed for user root
Jun 24 05:46:22 galelhiani sudo[5572]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop ; USER=root ; COMMAND=/usr/bin/systemctl restart smbd
Jun 24 05:46:22 galelhiani sudo[5572]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 05:46:22 galelhiani systemd[1]: Stopping Samba SMB Daemon...
Jun 24 05:46:22 galelhiani systemd[1]: smbd.service: Deactivated successfully.
Jun 24 05:46:22 galelhiani systemd[1]: Stopped Samba SMB Daemon.
Jun 24 05:46:22 galelhiani systemd[1]: Starting Samba SMB Daemon...
Jun 24 05:46:22 galelhiani systemd[1]: Started Samba SMB Daemon.
Jun 24 05:46:22 galelhiani sudo[5572]: pam_unix(sudo:session): session closed for user root
Jun 24 05:46:50 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:46:50 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:47:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:47:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:48:09 galelhiani smbd[5598]: pam_unix(samba:session): session opened for user galelhiani(uid=1000) by (uid=0)
Jun 24 05:48:10 galelhiani kernel: TCP: enp0s1: Driver has suspect GRO implementation, TCP performance may be compromised.
Jun 24 05:48:27 galelhiani gnome-shell[1575]: Object .Gjs_ui_messageTray_Notification (0xaaaaf3187720), has been already disposed — impossible to emit any signal on it. This might be caused by the object having been destroyed from C code using something such as destroy(), dispose(), or remove() vfuncs.
Jun 24 05:48:27 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 05:48:27 galelhiani gnome-shell[1575]: #0   aaaaf2ec8c78 i   resource:///org/gnome/shell/ui/messageTray.js:493 (e2b3f351f60 @ 69)
Jun 24 05:48:27 galelhiani gnome-shell[1575]: #1   aaaaf2ec8bd0 i   resource:///org/gnome/shell/ui/messageTray.js:489 (e2b3f351f10 @ 56)
Jun 24 05:48:27 galelhiani gnome-shell[1575]: #2   aaaaf2ec8b48 i   resource:///org/gnome/shell/ui/calendar.js:797 (e2b3f35e150 @ 22)
Jun 24 05:48:27 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 05:48:27 galelhiani gnome-shell[1575]: #0   aaaaf2ec8c78 i   resource:///org/gnome/shell/ui/messageTray.js:494 (e2b3f351f60 @ 84)
Jun 24 05:48:27 galelhiani gnome-shell[1575]: #1   aaaaf2ec8bd0 i   resource:///org/gnome/shell/ui/messageTray.js:489 (e2b3f351f10 @ 56)
Jun 24 05:48:27 galelhiani gnome-shell[1575]: #2   aaaaf2ec8b48 i   resource:///org/gnome/shell/ui/calendar.js:797 (e2b3f35e150 @ 22)
Jun 24 05:48:27 galelhiani gnome-shell[1575]: Object .Gjs_ui_messageTray_Notification (0xaaaaf3187720), has been already disposed — impossible to access it. This might be caused by the object having been destroyed from C code using something such as destroy(), dispose(), or remove() vfuncs.
Jun 24 05:50:13 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:50:13 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:50:17 galelhiani systemd[1462]: Started VTE child process 5605 launched by gnome-terminal-server process 2335.
Jun 24 05:50:28 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.gedit' requested by ':1.108' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 05:50:28 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.gedit'
Jun 24 05:50:28 galelhiani gnome-shell[1575]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 24 05:50:30 galelhiani gsd-color[1726]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 05:52:05 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:52:05 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:53:21 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:53:21 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:54:18 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:54:18 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:55:30 galelhiani systemd[1462]: vte-spawn-c0b20a7b-3aba-4444-a615-29dc12f7b270.scope: Consumed 5.824s CPU time.
Jun 24 05:55:30 galelhiani gnome-shell[1575]: JS ERROR: TypeError: this.actor is null
                                              _syncEnabled@resource:///org/gnome/shell/ui/windowManager.js:138:25
                                              onStopped@resource:///org/gnome/shell/ui/windowManager.js:150:35
                                              _makeEaseCallback/<@resource:///org/gnome/shell/ui/environment.js:151:22
                                              _easeActorProperty/<@resource:///org/gnome/shell/ui/environment.js:317:60
                                              _destroyWindowDone@resource:///org/gnome/shell/ui/windowManager.js:1596:21
                                              onStopped@resource:///org/gnome/shell/ui/windowManager.js:1564:39
                                              _makeEaseCallback/<@resource:///org/gnome/shell/ui/environment.js:151:22
                                              _easeActor/<@resource:///org/gnome/shell/ui/environment.js:240:64
Jun 24 05:55:30 galelhiani systemd[1462]: gnome-terminal-server.service: Consumed 13.349s CPU time.
Jun 24 05:55:30 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 05:55:30 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 05:55:33 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating via systemd: service name='org.gnome.Terminal' unit='gnome-terminal-server.service' requested by ':1.108' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 05:55:33 galelhiani systemd[1462]: Starting GNOME Terminal Server...
Jun 24 05:55:33 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.Terminal'
Jun 24 05:55:33 galelhiani systemd[1462]: Started GNOME Terminal Server.
Jun 24 05:55:33 galelhiani systemd[1462]: Started VTE child process 5688 launched by gnome-terminal-server process 5670.
Jun 24 06:01:45 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 06:01:45 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 06:12:13 galelhiani snapd[877]: storehelpers.go:914: cannot refresh: snap has no updates available: "bare", "core20", "core24", "firefox", "gnome-46-2404", "gtk-common-themes", "lxd", "snapd"
Jun 24 06:12:21 galelhiani snapd[877]: cache.go:243: removed 0 entries/    0 from downloads cache
Jun 24 06:12:22 galelhiani systemd[1]: Reloading.
Jun 24 06:12:22 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 06:12:22 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 06:12:22 galelhiani systemd[1]: Mounting Mount unit for mesa-2404, revision 1778...
Jun 24 06:12:22 galelhiani kernel: set_capacity_and_notify: 4 callbacks suppressed
Jun 24 06:12:22 galelhiani kernel: loop13: detected capacity change from 0 to 385528
Jun 24 06:12:22 galelhiani systemd[1]: Mounted Mount unit for mesa-2404, revision 1778.
Jun 24 06:12:22 galelhiani snapd[877]: services.go:1167: RemoveSnapServices - disabling snap.mesa-2404.component-monitor.service
Jun 24 06:12:22 galelhiani systemd[1]: Reloading.
Jun 24 06:12:22 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 06:12:22 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 06:12:23 galelhiani audit[5924]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.connect-plug-kernel-gpu-2404" pid=5924 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5925]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.disconnect-plug-kernel-gpu-2404" pid=5925 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5923]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.component-monitor" pid=5923 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5926]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.install" pid=5926 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.315:76): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.connect-plug-kernel-gpu-2404" pid=5924 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.315:77): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.disconnect-plug-kernel-gpu-2404" pid=5925 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.315:78): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.component-monitor" pid=5923 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.315:79): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.install" pid=5926 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5927]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.post-refresh" pid=5927 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.387:80): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.mesa-2404.hook.post-refresh" pid=5927 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5931]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.configure" pid=5931 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.555:81): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.configure" pid=5931 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5932]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.disconnect-plug-host-hunspell" pid=5932 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.667:82): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.disconnect-plug-host-hunspell" pid=5932 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5933]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.install" pid=5933 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.771:83): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.install" pid=5933 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5928]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap-update-ns.firefox" pid=5928 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.851:84): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap-update-ns.firefox" pid=5928 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5930]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.geckodriver" pid=5930 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani kernel: audit: type=1400 audit(1782281543.895:85): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.geckodriver" pid=5930 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5934]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.hook.post-refresh" pid=5934 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5929]: AVC apparmor="STATUS" operation="profile_replace" profile="unconfined" name="snap.firefox.firefox" pid=5929 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani audit[5936]: AVC apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="snap-update-ns.mesa-2404" pid=5936 comm="apparmor_parser"
Jun 24 06:12:23 galelhiani systemd[1]: Reloading.
Jun 24 06:12:24 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 06:12:24 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 06:12:24 galelhiani systemd[1]: Started snap.mesa-2404.hook.post-refresh-8d2c761f-80e5-4867-9e7c-0d3ae826dbfd.scope.
Jun 24 06:12:24 galelhiani systemd[1]: tmp-snap.rootfs_N1XJdc.mount: Deactivated successfully.
Jun 24 06:12:24 galelhiani systemd[1]: Reloading.
Jun 24 06:12:24 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 06:12:24 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 06:12:24 galelhiani systemd[1]: snap.mesa-2404.hook.post-refresh-8d2c761f-80e5-4867-9e7c-0d3ae826dbfd.scope: Deactivated successfully.
Jun 24 06:12:25 galelhiani snapd[877]: storehelpers.go:914: cannot refresh snap "mesa-2404": snap has no updates available
Jun 24 06:17:01 galelhiani CRON[6058]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 06:17:01 galelhiani CRON[6059]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 06:17:01 galelhiani CRON[6058]: pam_unix(cron:session): session closed for user root
Jun 24 06:25:01 galelhiani CRON[6065]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 06:25:01 galelhiani CRON[6066]: (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ))
Jun 24 06:25:01 galelhiani CRON[6065]: pam_unix(cron:session): session closed for user root
Jun 24 06:25:33 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.75' (uid=1000 pid=1575 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 06:25:33 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 06:25:33 galelhiani dbus-daemon[857]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 06:25:33 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 06:25:33 galelhiani gnome-shell[1575]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 06:25:35 galelhiani gdm-password][6078]: gkr-pam: unlocked login keyring
Jun 24 06:25:35 galelhiani NetworkManager[858]: <info>  [1782282335.3058] agent-manager: agent[6481f1c1170d2754,:1.75/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 06:25:35 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for software-update-available
Jun 24 06:25:35 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for livepatch
Jun 24 06:25:35 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.ArchiveManager1' requested by ':1.139' (uid=1000 pid=6083 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 06:25:35 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 06:25:35 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 06:25:35 galelhiani gnome-shell[1575]: DING: Detected async api for thumbnails
Jun 24 06:25:35 galelhiani gnome-shell[1575]: DING: GNOME nautilus 42.6
Jun 24 06:26:03 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 06:26:05 galelhiani sudo[6129]: pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/0 ruser=galelhiani rhost=  user=galelhiani
Jun 24 06:26:10 galelhiani sudo[6129]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop/git/devops/linux_system_storage ; USER=root ; COMMAND=/usr/sbin/mke2fs -m /dev/sdb1
Jun 24 06:26:10 galelhiani sudo[6129]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 06:26:10 galelhiani sudo[6129]: pam_unix(sudo:session): session closed for user root
Jun 24 06:26:40 galelhiani systemd[1]: Starting Daily apt upgrade and clean activities...
Jun 24 06:27:10 galelhiani apt-helper[6135]: E: Sub-process nm-online returned an error code (1)
Jun 24 06:27:14 galelhiani systemd[1]: Reloading.
Jun 24 06:27:14 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 06:27:14 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 06:27:14 galelhiani systemd[1]: Starting Daily apt download activities...
Jun 24 06:27:14 galelhiani systemd[1]: Reloading.
Jun 24 06:27:14 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 06:27:14 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 06:27:14 galelhiani systemd[1]: Stopping A high performance web server and a reverse proxy server...
Jun 24 06:27:14 galelhiani systemd[1]: nginx.service: Deactivated successfully.
Jun 24 06:27:14 galelhiani systemd[1]: Stopped A high performance web server and a reverse proxy server.
Jun 24 06:27:14 galelhiani systemd[1]: Starting A high performance web server and a reverse proxy server...
Jun 24 06:27:14 galelhiani systemd[1]: Started A high performance web server and a reverse proxy server.
Jun 24 06:27:20 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 06:27:20 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 06:27:21 galelhiani systemd[1]: apt-daily-upgrade.service: Deactivated successfully.
Jun 24 06:27:21 galelhiani systemd[1]: Finished Daily apt upgrade and clean activities.
Jun 24 06:27:21 galelhiani systemd[1]: apt-daily-upgrade.service: Consumed 7.421s CPU time.
Jun 24 06:27:44 galelhiani apt-helper[6458]: E: Sub-process nm-online returned an error code (1)
Jun 24 06:27:44 galelhiani systemd[1]: Starting Update APT News...
Jun 24 06:27:44 galelhiani systemd[1]: Starting Update the local ESM caches...
Jun 24 06:27:44 galelhiani systemd[1]: apt-news.service: Deactivated successfully.
Jun 24 06:27:44 galelhiani systemd[1]: Finished Update APT News.
Jun 24 06:27:45 galelhiani sudo[7207]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop/git/devops/linux_system_storage ; USER=root ; COMMAND=/usr/sbin/mke2fs -m /dev/vda1
Jun 24 06:27:45 galelhiani sudo[7207]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 06:27:45 galelhiani sudo[7207]: pam_unix(sudo:session): session closed for user root
Jun 24 06:27:46 galelhiani systemd[1]: esm-cache.service: Deactivated successfully.
Jun 24 06:27:46 galelhiani systemd[1]: Finished Update the local ESM caches.
Jun 24 06:27:50 galelhiani systemd[1]: apt-daily.service: Deactivated successfully.
Jun 24 06:27:50 galelhiani systemd[1]: Finished Daily apt download activities.
Jun 24 06:27:50 galelhiani systemd[1]: apt-daily.service: Consumed 3.085s CPU time.
Jun 24 06:27:51 galelhiani sudo[7372]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop/git/devops/linux_system_storage ; USER=root ; COMMAND=/usr/sbin/mke2fs -m /dev/sda1
Jun 24 06:27:51 galelhiani sudo[7372]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 06:27:51 galelhiani sudo[7372]: pam_unix(sudo:session): session closed for user root
Jun 24 06:29:06 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 06:29:06 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 06:29:14 galelhiani sudo[7377]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop/git/devops/linux_system_storage ; USER=root ; COMMAND=/usr/sbin/mke2fs -n /dev/sda1
Jun 24 06:29:14 galelhiani sudo[7377]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 06:29:14 galelhiani sudo[7377]: pam_unix(sudo:session): session closed for user root
Jun 24 06:29:32 galelhiani pkexec[7394]: pam_unix(polkit-1:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 06:29:32 galelhiani pkexec[7394]: galelhiani: Executing command [USER=root] [TTY=unknown] [CWD=/home/galelhiani] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Jun 24 06:29:46 galelhiani sudo[7402]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop/git/devops/linux_system_storage ; USER=root ; COMMAND=/usr/sbin/mke2fs -n /dev/vda1
Jun 24 06:29:46 galelhiani sudo[7402]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 06:29:46 galelhiani sudo[7402]: pam_unix(sudo:session): session closed for user root
Jun 24 06:34:01 galelhiani systemd[1462]: gnome-terminal-server.service: Consumed 2.078s CPU time.
Jun 24 06:35:18 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 06:35:18 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 06:35:48 galelhiani systemd[1]: fwupd.service: Deactivated successfully.
Jun 24 06:39:08 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 06:39:08 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 06:47:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 06:47:28 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 07:13:03 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.75' (uid=1000 pid=1575 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 07:13:03 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 07:13:03 galelhiani dbus-daemon[857]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 07:13:03 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 07:13:03 galelhiani gnome-shell[1575]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 07:13:05 galelhiani gdm-password][7476]: gkr-pam: unlocked login keyring
Jun 24 07:13:05 galelhiani NetworkManager[858]: <info>  [1782285185.4270] agent-manager: agent[1179fd472d090239,:1.75/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 07:13:05 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for software-update-available
Jun 24 07:13:05 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for livepatch
Jun 24 07:13:05 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.ArchiveManager1' requested by ':1.144' (uid=1000 pid=7481 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 07:13:05 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 07:13:05 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 07:13:05 galelhiani gnome-shell[1575]: DING: Detected async api for thumbnails
Jun 24 07:13:05 galelhiani gnome-shell[1575]: DING: GNOME nautilus 42.6
Jun 24 07:13:06 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.106' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 07:13:06 galelhiani systemd[1]: Starting Hostname Service...
Jun 24 07:13:06 galelhiani dbus-daemon[857]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 24 07:13:06 galelhiani systemd[1]: Started Hostname Service.
Jun 24 07:13:33 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 07:13:36 galelhiani systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 24 07:15:42 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.gedit' requested by ':1.108' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 07:15:42 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.gedit'
Jun 24 07:15:42 galelhiani gnome-shell[1575]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 24 07:17:01 galelhiani CRON[7568]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 07:17:01 galelhiani CRON[7569]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 07:17:01 galelhiani CRON[7568]: pam_unix(cron:session): session closed for user root
Jun 24 07:17:46 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.106' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 07:17:46 galelhiani systemd[1]: Starting Hostname Service...
Jun 24 07:17:46 galelhiani dbus-daemon[857]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 24 07:17:46 galelhiani systemd[1]: Started Hostname Service.
Jun 24 07:25:13 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:25:43 galelhiani systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 24 07:29:21 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:30:01 galelhiani CRON[7600]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 07:30:01 galelhiani CRON[7601]: (root) CMD ([ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi)
Jun 24 07:30:01 galelhiani CRON[7600]: pam_unix(cron:session): session closed for user root
Jun 24 07:30:52 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 07:30:52 galelhiani update-notifier[2078]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 07:36:17 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:36:17 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 07:36:17 galelhiani anacron[7617]: Anacron 2.3 started on 2026-06-24
Jun 24 07:36:17 galelhiani anacron[7617]: Will run job `cron.daily' in 5 min.
Jun 24 07:36:17 galelhiani anacron[7617]: Jobs will be executed sequentially
Jun 24 07:38:22 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:38:55 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.75' (uid=1000 pid=1575 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 07:38:55 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 07:38:55 galelhiani dbus-daemon[857]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 07:38:55 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 07:38:55 galelhiani gnome-shell[1575]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 07:38:58 galelhiani gdm-password][7638]: pam_unix(gdm-password:auth): authentication failure; logname= uid=0 euid=0 tty=/dev/tty1 ruser= rhost=  user=galelhiani
Jun 24 07:39:02 galelhiani gdm-password][7642]: gkr-pam: unlocked login keyring
Jun 24 07:39:02 galelhiani NetworkManager[858]: <info>  [1782286742.8229] agent-manager: agent[1179fd472d090239,:1.75/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 07:39:02 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for software-update-available
Jun 24 07:39:02 galelhiani ubuntu-appindicators@ubuntu.com[1575]: unable to update icon for livepatch
Jun 24 07:39:02 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.ArchiveManager1' requested by ':1.151' (uid=1000 pid=7646 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 07:39:02 galelhiani gnome-shell[1575]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 07:39:03 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 07:39:03 galelhiani gnome-shell[1575]: DING: Detected async api for thumbnails
Jun 24 07:39:03 galelhiani gnome-shell[1575]: DING: GNOME nautilus 42.6
Jun 24 07:39:26 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 07:41:45 galelhiani anacron[7617]: Job `cron.daily' started
Jun 24 07:41:45 galelhiani anacron[7706]: Updated timestamp for job `cron.daily' to 2026-06-24
Jun 24 07:41:45 galelhiani cracklib[7728]: no dictionary update necessary.
Jun 24 07:41:45 galelhiani anacron[7617]: Job `cron.daily' terminated
Jun 24 07:41:45 galelhiani anacron[7617]: Normal exit (1 job run)
Jun 24 07:41:45 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 07:42:18 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:42:51 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:43:57 galelhiani systemd-resolved[845]: Clock change detected. Flushing caches.
Jun 24 07:44:04 galelhiani dbus-daemon[857]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.106' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 07:44:04 galelhiani systemd[1]: Starting Hostname Service...
Jun 24 07:44:04 galelhiani dbus-daemon[857]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 24 07:44:04 galelhiani systemd[1]: Started Hostname Service.
Jun 24 07:44:12 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating service name='org.gnome.gedit' requested by ':1.108' (uid=1000 pid=2262 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 07:44:12 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.gedit'
Jun 24 07:44:12 galelhiani gnome-shell[1575]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 24 07:44:34 galelhiani systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 24 07:46:33 galelhiani systemd[1462]: Started Application launched by gnome-shell.
Jun 24 07:46:33 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Activating via systemd: service name='org.gnome.Terminal' unit='gnome-terminal-server.service' requested by ':1.158' (uid=1000 pid=7784 comm="/usr/bin/gnome-terminal.real " label="unconfined")
Jun 24 07:46:33 galelhiani systemd[1462]: Starting GNOME Terminal Server...
Jun 24 07:46:33 galelhiani dbus-daemon[1482]: [session uid=1000 pid=1482] Successfully activated service 'org.gnome.Terminal'
Jun 24 07:46:33 galelhiani systemd[1462]: Started GNOME Terminal Server.
Jun 24 07:46:33 galelhiani systemd[1462]: Started VTE child process 7807 launched by gnome-terminal-server process 7789.
Jun 24 07:46:58 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 07:46:58 galelhiani parcellite-startup.desktop[1965]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 07:52:47 galelhiani gnome-shell[1575]: endSessionDialog: No XDG_SESSION_ID, fetched from logind: 2
Jun 24 07:52:49 galelhiani systemd[1]: unattended-upgrades.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd-logind[890]: System is powering down.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Session 2 of User galelhiani...
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was notify on NMDeviceEthernet 0xaaaaf4ad42a0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was state-changed on NMDeviceEthernet 0xaaaaf4ad42a0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: == Stack trace for context 0xaaaaf2cfa490 ==
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3e3ce00.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3e3ce00.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3e3ce00.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3e3ce00.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf3d3faa0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf393cc60.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf393cc60.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf393cc60.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf393cc60.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf7a55210.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf32b94d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf32b94d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf32b94d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf32b94d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf7803240.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf40d8f10.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf40d8f10.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf40d8f10.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf40d8f10.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf7568990.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4b0bdd0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4b0bdd0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4b0bdd0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4b0bdd0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf7a5ca30.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf53d37b0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf53d37b0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf53d37b0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf53d37b0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf4aec380.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf468f5d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf468f5d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf468f5d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf468f5d0.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf3d39960.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4af3930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4af3930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4af3930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf4af3930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf3d74520.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3d5b860.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3d5b860.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3d5b860.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf3d5b860.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf3d63d30.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7ad0150.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7ad0150.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7ad0150.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7ad0150.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf7abeb20.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7a62930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7a62930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7a62930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_appDisplay_AppIcon 0xaaaaf7a62930.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was destroy on Gjs_ui_iconGrid_BaseIcon 0xaaaaf4f66490.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to call back into JSAPI during the sweeping phase of GC. This is most likely caused by not destroying a Clutter actor or Gtk+ widget with ::destroy signals connected, but can also be caused by using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked and the JS callback not invoked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending signal was actor-removed on Gjs_ui_appDisplay_FolderGrid 0xaaaaf3e3d670.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: Attempting to run a JS callback during garbage collection. This is most likely caused by destroying a Clutter actor or GTK widget with ::destroy signal connected, or using the destroy(), dispose(), or remove() vfuncs. Because it would crash the application, it has been blocked.
Jun 24 07:52:49 galelhiani gnome-shell[1575]: The offending callback was set_container(), a vfunc.
Jun 24 07:52:49 galelhiani systemd[1]: Removed slice Slice /system/getty.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Wayland Session (session: ubuntu).
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Session.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME session X11 services.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Session (session: ubuntu).
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME accessibility target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME color management target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME date & time target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME maintenance of expirable data target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME keyboard configuration target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME keyboard shortcuts target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME power management target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME printer notifications target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME RFKill support target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME FreeDesktop screensaver target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME file sharing target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME smartcard target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME sound sample caching target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Wacom tablet support target.
Jun 24 07:52:49 galelhiani systemd[1]: Removed slice Slice /system/modprobe.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME XSettings target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping IBus Daemon for GNOME...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Cloud-init target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME color management service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Preparation for Logins.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME date & time service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Graphical Interface.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME keyboard configuration service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Sound Card.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME keyboard shortcuts service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Timer Units.
Jun 24 07:52:49 galelhiani systemd[1]: anacron.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME power management service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Trigger anacron every hour.
Jun 24 07:52:49 galelhiani systemd[1]: apt-daily-upgrade.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME printer notifications service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daily apt upgrade and clean activities.
Jun 24 07:52:49 galelhiani systemd[1]: apt-daily.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME RFKill support service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daily apt download activities.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME file sharing service...
Jun 24 07:52:49 galelhiani systemd[1]: dpkg-db-backup.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daily dpkg database backup timer.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME sound sample caching service...
Jun 24 07:52:49 galelhiani systemd[1]: e2scrub_all.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME Wacom tablet support service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Periodic ext4 Online Metadata Check for All Filesystems.
Jun 24 07:52:49 galelhiani systemd[1]: fstrim.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping GNOME XSettings service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Discard unused blocks once a week.
Jun 24 07:52:49 galelhiani systemd[1]: fwupd-refresh.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Refresh fwupd metadata regularly.
Jun 24 07:52:49 galelhiani systemd[1]: logrotate.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daily rotation of log files.
Jun 24 07:52:49 galelhiani systemd[1]: man-db.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daily man-db regeneration.
Jun 24 07:52:49 galelhiani systemd[1]: motd-news.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Message of the Day.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-tmpfiles-clean.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daily Cleanup of Temporary Directories.
Jun 24 07:52:49 galelhiani systemd[1]: update-notifier-download.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Download data for packages that failed at package install time.
Jun 24 07:52:49 galelhiani systemd[1]: update-notifier-motd.timer: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Check to see whether there is a new version of Ubuntu available.
Jun 24 07:52:49 galelhiani systemd[1]: cloud-init-hotplugd.socket: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Closed cloud-init hotplug hook socket.
Jun 24 07:52:49 galelhiani systemd[1]: lvm2-lvmpolld.socket: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Closed LVM2 poll daemon socket.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-rfkill.socket: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Closed Load/Save RF Kill Switch Status /dev/rfkill Watch.
Jun 24 07:52:49 galelhiani kernel: rfkill: input handler enabled
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Wayland Session.
Jun 24 07:52:49 galelhiani ModemManager[909]: <info>  caught signal, shutting down...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Current graphical user session.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Accounts Service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Save/Restore Sound Card State...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Availability of block devices...
Jun 24 07:52:49 galelhiani systemd[1]: cloud-final.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Cloud-init: Final Stage.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Multi-User System.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Login Prompts.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Modem Manager...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping LSB: automatic crash report generation...
Jun 24 07:52:49 galelhiani blkdeactivate[7855]: Deactivating block devices:
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Deferred execution scheduler...
Jun 24 07:52:49 galelhiani systemd[1]: cloud-config.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Cloud-init: Config Stage.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Cloud-config availability.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Manage, Install and Generate Color Profiles...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Regular background program processing daemon...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Make remote CUPS printers available locally...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Create final runtime dir for shutdown pivot root...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping GNOME Display Manager...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Location Lookup Service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping irqbalance daemon...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Tool to automatically collect and submit kernel crash signatures...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Path trigger for Apport crash notifications.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping LVM event activation on device 252:3...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Dispatcher daemon for systemd-networkd...
Jun 24 07:52:49 galelhiani NetworkManager[858]: <info>  [1782287569.0683] modem-manager: ModemManager no longer available
Jun 24 07:52:49 galelhiani systemd[1]: Stopping A high performance web server and a reverse proxy server...
Jun 24 07:52:49 galelhiani systemd[1]: openvpn.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped OpenVPN service.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping PackageKit Daemon...
Jun 24 07:52:49 galelhiani systemd[1]: plymouth-quit-wait.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Hold until boot process finishes up.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Power Profiles daemon...
Jun 24 07:52:49 galelhiani snapd[877]: main.go:168: Exiting on terminated signal.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping System Logging Service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping RealtimeKit Scheduling Policy Service...
Jun 24 07:52:49 galelhiani sshd[1051]: Received signal 15; terminating.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Samba SMB Daemon...
Jun 24 07:52:49 galelhiani smbd[5598]: pam_unix(samba:session): session closed for user galelhiani
Jun 24 07:52:49 galelhiani lvm[7869]:   pvscan[7869] PV /dev/vda3 online.
Jun 24 07:52:49 galelhiani blkdeactivate[7855]:   [SKIP]: unmount of ubuntu--vg-ubuntu--lv (dm-0) mounted on /
Jun 24 07:52:49 galelhiani systemd[1]: snapd.seeded.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani ModemManager[909]: <info>  ModemManager is shut down
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Wait until snapd is fully seeded.
Jun 24 07:52:49 galelhiani rsyslogd[873]: [origin software="rsyslogd" swVersion="8.2112.0" x-pid="873" x-info="https://www.rsyslog.com"] exiting on signal 15.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Snap Daemon...
Jun 24 07:52:49 galelhiani systemd[1]: Condition check resulted in Ubuntu core (all-snaps) system shutdown helper setup service being skipped.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Agent daemon for Spice guests...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping OpenBSD Secure Shell server...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Path trigger for new release of Ubuntu notifications.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Load/Save Random Seed...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Disk Manager...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Daemon for power management...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped IBus Daemon for GNOME.
Jun 24 07:52:49 galelhiani systemd[1462]: org.freedesktop.IBus.session.GNOME.service: Consumed 7.463s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: irqbalance.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped irqbalance daemon.
Jun 24 07:52:49 galelhiani systemd[1]: irqbalance.service: Consumed 5.133s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: networkd-dispatcher.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Dispatcher daemon for systemd-networkd.
Jun 24 07:52:49 galelhiani systemd[1]: rsyslog.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped System Logging Service.
Jun 24 07:52:49 galelhiani systemd[1]: ModemManager.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Modem Manager.
Jun 24 07:52:49 galelhiani systemd[1]: cron.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Regular background program processing daemon.
Jun 24 07:52:49 galelhiani systemd[1]: atd.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Deferred execution scheduler.
Jun 24 07:52:49 galelhiani systemd[1]: ssh.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped OpenBSD Secure Shell server.
Jun 24 07:52:49 galelhiani systemd[1]: rtkit-daemon.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped RealtimeKit Scheduling Policy Service.
Jun 24 07:52:49 galelhiani systemd[1]: rtkit-daemon.service: Consumed 1.725s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: colord.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Manage, Install and Generate Color Profiles.
Jun 24 07:52:49 galelhiani systemd[1]: alsa-restore.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Save/Restore Sound Card State.
Jun 24 07:52:49 galelhiani systemd[1]: kerneloops.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Tool to automatically collect and submit kernel crash signatures.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME FreeDesktop screensaver service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME date & time service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME maintenance of expirable data service.
Jun 24 07:52:49 galelhiani systemd[1462]: org.gnome.SettingsDaemon.Housekeeping.service: Consumed 1.620s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME printer notifications service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME RFKill support service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME file sharing service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME sound sample caching service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME XSettings service.
Jun 24 07:52:49 galelhiani systemd[1]: packagekit.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani udisksd[893]: udisks daemon version 2.9.4 exiting
Jun 24 07:52:49 galelhiani systemd[1]: Stopped PackageKit Daemon.
Jun 24 07:52:49 galelhiani systemd[1]: packagekit.service: Consumed 4.680s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: blk-availability.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Availability of block devices.
Jun 24 07:52:49 galelhiani systemd[1]: nginx.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped A high performance web server and a reverse proxy server.
Jun 24 07:52:49 galelhiani evolution-alarm[1977]: Error reading events from display: Broken pipe
Jun 24 07:52:49 galelhiani systemd[1]: smbd.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Samba SMB Daemon.
Jun 24 07:52:49 galelhiani systemd[1]: session-2.scope: Deactivated successfully.
Jun 24 07:52:49 galelhiani xdg-desktop-por[1937]: Error reading events from display: Broken pipe
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Session 2 of User galelhiani.
Jun 24 07:52:49 galelhiani xdg-desktop-por[1846]: Error reading events from display: Broken pipe
Jun 24 07:52:49 galelhiani systemd[1]: geoclue.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Location Lookup Service.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-random-seed.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Load/Save Random Seed.
Jun 24 07:52:49 galelhiani update-notifier[2078]: Error reading events from display: Broken pipe
Jun 24 07:52:49 galelhiani gnome-shell[1828]: (EE) failed to read Wayland events: Connection reset by peer
Jun 24 07:52:49 galelhiani nautilus[2262]: Error reading events from display: Broken pipe
Jun 24 07:52:49 galelhiani systemd-logind[890]: Session 2 logged out. Waiting for processes to exit.
Jun 24 07:52:49 galelhiani parcellite-startup.desktop[1965]: parcellite: Fatal IO error 11 (Resource temporarily unavailable) on X server :0.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Host and Network Name Lookups.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Samba NMB Daemon...
Jun 24 07:52:49 galelhiani apport[7862]:  * Stopping automatic crash report generation: apport
Jun 24 07:52:49 galelhiani apport[7862]:    ...done.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Authorization Manager...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Switcheroo Control Proxy service...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping User Login Management...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping User Manager for UID 1000...
Jun 24 07:52:49 galelhiani systemd[1462]: org.gnome.Shell@wayland.service: Killing process 7652 (JS Helper) with signal SIGKILL.
Jun 24 07:52:49 galelhiani systemd[1]: accounts-daemon.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Accounts Service.
Jun 24 07:52:49 galelhiani systemd[1]: accounts-daemon.service: Consumed 2.406s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: udisks2.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Disk Manager.
Jun 24 07:52:49 galelhiani systemd[1]: nmbd.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Samba NMB Daemon.
Jun 24 07:52:49 galelhiani systemd[1]: apport.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped LSB: automatic crash report generation.
Jun 24 07:52:49 galelhiani systemd[1]: power-profiles-daemon.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Power Profiles daemon.
Jun 24 07:52:49 galelhiani systemd[1]: upower.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Daemon for power management.
Jun 24 07:52:49 galelhiani systemd[1]: lvm2-pvscan@252:3.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped LVM event activation on device 252:3.
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-desktop-portal-gnome.service: Main process exited, code=exited, status=1/FAILURE
Jun 24 07:52:49 galelhiani systemd[1]: Removed slice Slice /system/lvm2-pvscan.
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-desktop-portal-gnome.service: Failed with result 'exit-code'.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Portal service (GNOME implementation).
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-desktop-portal-gtk.service: Main process exited, code=exited, status=1/FAILURE
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-desktop-portal-gtk.service: Failed with result 'exit-code'.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Portal service (GTK/GNOME implementation).
Jun 24 07:52:49 galelhiani systemd-logind[890]: Removed session 2.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME color management service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME keyboard configuration service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME keyboard shortcuts service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME power management service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME Wacom tablet support service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Application launched by gnome-session-binary.
Jun 24 07:52:49 galelhiani systemd[1462]: app-gnome-spice\x2dvdagent-1817.scope: Consumed 57.309s CPU time.
Jun 24 07:52:49 galelhiani systemd-tmpfiles[8023]: /run/finalrd-libs.conf:8: Duplicate line for path "/run/initramfs/lib", ignoring.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Application launched by gnome-session-binary.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Application launched by gnome-session-binary.
Jun 24 07:52:49 galelhiani systemd[1462]: app-gnome-update\x2dnotifier-2078.scope: Consumed 6.357s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Application launched by gnome-session-binary.
Jun 24 07:52:49 galelhiani systemd[1462]: app-gnome-parcellite\x2dstartup-1965.scope: Consumed 2min 30.518s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME Shell on Wayland.
Jun 24 07:52:49 galelhiani systemd[1462]: org.gnome.Shell@wayland.service: Consumed 22min 3.012s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Monitor Session leader for GNOME Session.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Application launched by gnome-session-binary...
Jun 24 07:52:49 galelhiani systemd[1462]: Removed slice Slice /app/org.gnome.Terminal.
Jun 24 07:52:49 galelhiani systemd[1462]: app-org.gnome.Terminal.slice: Consumed 22.474s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Main User Target.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME session X11 services.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Session is initialized.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Session Manager is ready.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target GNOME Shell.
Jun 24 07:52:49 galelhiani gvfsd[1537]: A connection to the bus can't be made
Jun 24 07:52:49 galelhiani gvfsd[1692]: A connection to the bus can't be made
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping D-Bus User Message Bus...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping User preferences database...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Evolution address book service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Evolution calendar service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Evolution source registry...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem service - Apple File Conduit monitor...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem service - GNOME Online Accounts monitor...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem service - digital camera monitor...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem metadata service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem service - Media Transfer Protocol monitor...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Virtual filesystem service - disk device monitor...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping PipeWire Media Session Manager...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Tracker file system data miner...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Portal service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping flatpak document portal service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping sandboxed app permission store...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped PipeWire Media Session Manager.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped D-Bus User Message Bus.
Jun 24 07:52:49 galelhiani systemd[1462]: dbus.service: Consumed 15.359s CPU time.
Jun 24 07:52:49 galelhiani tracker-miner-f[1948]: Owner of volume monitor org.gtk.vfs.UDisks2VolumeMonitor disconnected from the bus; removing drives/volumes/mounts
Jun 24 07:52:49 galelhiani tracker-miner-f[1948]: Owner of volume monitor org.gtk.vfs.GoaVolumeMonitor disconnected from the bus; removing drives/volumes/mounts
Jun 24 07:52:49 galelhiani finalrd[8036]: run-parts: executing /usr/share/finalrd/mdadm.finalrd setup
Jun 24 07:52:49 galelhiani tracker-miner-f[1948]: Owner of volume monitor org.gtk.vfs.GPhoto2VolumeMonitor disconnected from the bus; removing drives/volumes/mounts
Jun 24 07:52:49 galelhiani tracker-miner-f[1948]: Owner of volume monitor org.gtk.vfs.MTPVolumeMonitor disconnected from the bus; removing drives/volumes/mounts
Jun 24 07:52:49 galelhiani tracker-miner-f[1948]: Owner of volume monitor org.gtk.vfs.AfcVolumeMonitor disconnected from the bus; removing drives/volumes/mounts
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem service.
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-permission-store.service: Main process exited, code=exited, status=1/FAILURE
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-permission-store.service: Failed with result 'exit-code'.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped sandboxed app permission store.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Evolution source registry.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Evolution calendar service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem service - disk device monitor.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem service - GNOME Online Accounts monitor.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped User preferences database.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem service - digital camera monitor.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem service - Media Transfer Protocol monitor.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem service - Apple File Conduit monitor.
Jun 24 07:52:49 galelhiani systemd[1462]: gvfs-afc-volume-monitor.service: Consumed 7.393s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Portal service.
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-desktop-portal.service: Consumed 3.166s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-document-portal.service: Main process exited, code=exited, status=20/n/a
Jun 24 07:52:49 galelhiani systemd[1462]: xdg-document-portal.service: Failed with result 'exit-code'.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped flatpak document portal service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Virtual filesystem metadata service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped GNOME Session Manager (session: ubuntu).
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Application launched by gnome-session-binary.
Jun 24 07:52:49 galelhiani systemd[1462]: Removed slice Slice /app/gnome-session-manager.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Tasks to be run before GNOME Session starts.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Session services which should run early before the graphical session is brought up.
Jun 24 07:52:49 galelhiani systemd[1462]: Reached target Shutdown running GNOME Session.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping Start gnome-keyring as SSH agent...
Jun 24 07:52:49 galelhiani systemd[1462]: Starting Restart DBus after GNOME Session shutdown...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopping PipeWire Multimedia Service...
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped PipeWire Multimedia Service.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Shutdown running GNOME Session.
Jun 24 07:52:49 galelhiani sh[8043]: dbus-update-activation-environment: error: unable to connect to D-Bus: Did not receive a reply. Possible causes include: the remote application did not send a reply, the message bus security policy blocked the reply, the reply timeout expired, or the network connection was broken.
Jun 24 07:52:49 galelhiani systemd[1462]: Started Restart DBus after GNOME Session shutdown.
Jun 24 07:52:49 galelhiani systemd[1462]: gnome-keyring-ssh.service: Control process exited, code=exited, status=71/OSERR
Jun 24 07:52:49 galelhiani systemd[1462]: gnome-keyring-ssh.service: Failed with result 'exit-code'.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Start gnome-keyring as SSH agent.
Jun 24 07:52:49 galelhiani gnome-session-c[8042]: Couldn't connect to session bus: Error receiving data: Connection reset by peer
Jun 24 07:52:49 galelhiani spice-vdagentd[1433]: vdagentd quitting, returning status 0
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Evolution address book service.
Jun 24 07:52:49 galelhiani gdm3[1081]: Gdm: GdmLocalDisplayFactory: Failed to issue method call: GDBus.Error:org.freedesktop.DBus.Error.NoReply: Message recipient disconnected from message bus without replying
Jun 24 07:52:49 galelhiani gdm3[1081]: Gdm: Freeing conversation 'gdm-password' with active job
Jun 24 07:52:49 galelhiani finalrd[8036]: run-parts: executing /usr/share/finalrd/open-iscsi.finalrd setup
Jun 24 07:52:49 galelhiani systemd[1]: run-user-1000-doc.mount: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Unmounted /run/user/1000/doc.
Jun 24 07:52:49 galelhiani systemd[1]: run-user-1000-gvfs.mount: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Unmounted /run/user/1000/gvfs.
Jun 24 07:52:49 galelhiani tracker-miner-fs-3[1948]: OK
Jun 24 07:52:49 galelhiani pulseaudio[1471]: Error opening PCM device hw:0: No such file or directory
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Tracker file system data miner.
Jun 24 07:52:49 galelhiani systemd[1462]: tracker-miner-fs-3.service: Consumed 1.252s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Removed slice User Background Tasks Slice.
Jun 24 07:52:49 galelhiani systemd[1462]: background.slice: Consumed 1.284s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Sound Service.
Jun 24 07:52:49 galelhiani systemd[1462]: Removed slice User Core Session Slice.
Jun 24 07:52:49 galelhiani systemd[1462]: session.slice: Consumed 22min 17.199s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Basic System.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Paths.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped Pending report trigger for Ubuntu Report.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Sockets.
Jun 24 07:52:49 galelhiani systemd[1462]: Stopped target Timers.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed D-Bus User Message Bus Socket.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed GnuPG network certificate management daemon.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 24 07:52:49 galelhiani systemd[1462]: Closed GnuPG cryptographic agent and passphrase cache (restricted).
Jun 24 07:52:49 galelhiani systemd[1462]: Closed GnuPG cryptographic agent (ssh-agent emulation).
Jun 24 07:52:49 galelhiani systemd[1462]: Closed GnuPG cryptographic agent and passphrase cache.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed PipeWire Multimedia System Socket.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed debconf communication socket.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed Sound System.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed REST API socket for snapd user session agent.
Jun 24 07:52:49 galelhiani systemd[1462]: Closed Speech Dispatcher Socket.
Jun 24 07:52:49 galelhiani systemd[1462]: Removed slice User Application Slice.
Jun 24 07:52:49 galelhiani systemd[1462]: app.slice: Consumed 4min 20.778s CPU time.
Jun 24 07:52:49 galelhiani systemd[1462]: Reached target Shutdown.
Jun 24 07:52:49 galelhiani systemd[1462]: Finished Exit the Session.
Jun 24 07:52:49 galelhiani systemd[1462]: Reached target Exit the Session.
Jun 24 07:52:49 galelhiani systemd[1]: polkit.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Authorization Manager.
Jun 24 07:52:49 galelhiani systemd[1]: gdm.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped GNOME Display Manager.
Jun 24 07:52:49 galelhiani systemd[1]: spice-vdagentd.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Agent daemon for Spice guests.
Jun 24 07:52:49 galelhiani systemd[1]: spice-vdagentd.service: Consumed 26.846s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: cups-browsed.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Make remote CUPS printers available locally.
Jun 24 07:52:49 galelhiani systemd[1]: user@1000.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped User Manager for UID 1000.
Jun 24 07:52:49 galelhiani systemd[1]: user@1000.service: Consumed 26min 39.834s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Network is Online.
Jun 24 07:52:49 galelhiani systemd[1]: NetworkManager-wait-online.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Network Manager Wait Online.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Avahi mDNS/DNS-SD Stack...
Jun 24 07:52:49 galelhiani avahi-daemon[856]: Got SIGTERM, quitting.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping CUPS Scheduler...
Jun 24 07:52:49 galelhiani avahi-daemon[856]: Leaving mDNS multicast group on interface enp0s1.IPv6 with address fd2f:59a9:1813:5d8e:78e6:46ff:fe77:bc66.
Jun 24 07:52:49 galelhiani systemd[1]: Condition check resulted in Show Plymouth Power Off Screen being skipped.
Jun 24 07:52:49 galelhiani avahi-daemon[856]: Leaving mDNS multicast group on interface enp0s1.IPv4 with address 192.168.64.2.
Jun 24 07:52:49 galelhiani avahi-daemon[856]: Leaving mDNS multicast group on interface lo.IPv6 with address ::1.
Jun 24 07:52:49 galelhiani avahi-daemon[856]: Leaving mDNS multicast group on interface lo.IPv4 with address 127.0.0.1.
Jun 24 07:52:49 galelhiani systemd[1]: Starting Tell Plymouth To Jump To initramfs...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Userspace Out-Of-Memory (OOM) Killer...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping User Runtime Directory /run/user/1000...
Jun 24 07:52:49 galelhiani systemd[1]: run-user-1000.mount: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Unmounted /run/user/1000.
Jun 24 07:52:49 galelhiani systemd[1]: user-runtime-dir@1000.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped User Runtime Directory /run/user/1000.
Jun 24 07:52:49 galelhiani systemd[1]: switcheroo-control.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Switcheroo Control Proxy service.
Jun 24 07:52:49 galelhiani systemd[1]: Removed slice User Slice of UID 1000.
Jun 24 07:52:49 galelhiani systemd[1]: user-1000.slice: Consumed 26min 40.175s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Permit User Sessions...
Jun 24 07:52:49 galelhiani systemd[1]: systemd-user-sessions.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Permit User Sessions.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Remote File Systems.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Preparation for Remote File Systems.
Jun 24 07:52:49 galelhiani avahi-daemon[856]: avahi-daemon 0.8 exiting.
Jun 24 07:52:49 galelhiani systemd[1]: avahi-daemon.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Avahi mDNS/DNS-SD Stack.
Jun 24 07:52:49 galelhiani systemd[1]: avahi-daemon.service: Consumed 3.061s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: cups.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped CUPS Scheduler.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target Network.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Network Manager...
Jun 24 07:52:49 galelhiani NetworkManager[858]: <info>  [1782287569.2319] caught SIGTERM, shutting down normally.
Jun 24 07:52:49 galelhiani systemd[1]: Stopping Network Name Resolution...
Jun 24 07:52:49 galelhiani systemd[1]: Stopping WPA supplicant...
Jun 24 07:52:49 galelhiani systemd[1]: Finished Tell Plymouth To Jump To initramfs.
Jun 24 07:52:49 galelhiani systemd[1]: wpa_supplicant.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped WPA supplicant.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-logind.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped User Login Management.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped target User and Group Name Lookups.
Jun 24 07:52:49 galelhiani NetworkManager[858]: <info>  [1782287569.2475] exiting (success)
Jun 24 07:52:49 galelhiani systemd[1]: NetworkManager.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Network Manager.
Jun 24 07:52:49 galelhiani systemd[1]: NetworkManager.service: Consumed 2.766s CPU time.
Jun 24 07:52:49 galelhiani systemd[1]: finalrd.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Create final runtime dir for shutdown pivot root.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-resolved.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Network Name Resolution.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-oomd.service: Deactivated successfully.
Jun 24 07:52:49 galelhiani systemd[1]: Stopped Userspace Out-Of-Memory (OOM) Killer.
Jun 24 07:52:49 galelhiani systemd[1]: systemd-oomd.service: Consumed 1min 43.322s CPU time.
Jun 24 07:52:52 galelhiani snapd[877]: standby.go:121: standby monitoring stop requested
Jun 24 07:52:52 galelhiani snapd[877]: overlord.go:558: Released state lock file
Jun 24 07:52:52 galelhiani systemd[1]: snapd.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Snap Daemon.
Jun 24 07:52:52 galelhiani systemd[1]: snapd.service: Consumed 10.477s CPU time.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Basic System.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Path Units.
Jun 24 07:52:52 galelhiani systemd[1]: cups.path: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped CUPS Scheduler.
Jun 24 07:52:52 galelhiani systemd[1]: whoopsie.path: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Start whoopsie on modification of the /var/crash directory.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Slice Units.
Jun 24 07:52:52 galelhiani systemd[1]: Removed slice User and Session Slice.
Jun 24 07:52:52 galelhiani systemd[1]: user.slice: Consumed 26min 42.890s CPU time.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Socket Units.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target System Time Set.
Jun 24 07:52:52 galelhiani systemd[1]: avahi-daemon.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Avahi mDNS/DNS-SD Stack Activation Socket.
Jun 24 07:52:52 galelhiani systemd[1]: cups.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed CUPS Scheduler.
Jun 24 07:52:52 galelhiani systemd[1]: iscsid.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Open-iSCSI iscsid Socket.
Jun 24 07:52:52 galelhiani systemd[1]: snap.lxd.daemon.unix.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Socket unix for snap application lxd.daemon.
Jun 24 07:52:52 galelhiani systemd[1]: snap.lxd.user-daemon.unix.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Socket unix for snap application lxd.user-daemon.
Jun 24 07:52:52 galelhiani systemd[1]: snapd.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Socket activation for snappy daemon.
Jun 24 07:52:52 galelhiani systemd[1]: spice-vdagentd.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Activation socket for spice guest agent daemon.
Jun 24 07:52:52 galelhiani systemd[1]: syslog.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Syslog Socket.
Jun 24 07:52:52 galelhiani systemd[1]: uuidd.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed UUID daemon activation socket.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target System Initialization.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Local Encrypted Volumes.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-ask-password-console.path: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Dispatch Password Requests to Console Directory Watch.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-ask-password-wall.path: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Forward Password Requests to Wall Directory Watch.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Local Verity Protected Volumes.
Jun 24 07:52:52 galelhiani systemd[1]: cloud-init.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Cloud-init: Network Stage.
Jun 24 07:52:52 galelhiani systemd[1]: Stopping Set Up Additional Binary Formats...
Jun 24 07:52:52 galelhiani systemd[1]: systemd-networkd-wait-online.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Wait for Network to be Configured.
Jun 24 07:52:52 galelhiani systemd[1]: Stopping Network Configuration...
Jun 24 07:52:52 galelhiani systemd-networkd[843]: enp0s1: DHCP lease lost
Jun 24 07:52:52 galelhiani systemd[1]: Stopping Network Time Synchronization...
Jun 24 07:52:52 galelhiani systemd[1]: Stopping Record System Boot/Shutdown in UTMP...
Jun 24 07:52:52 galelhiani systemd[1]: systemd-binfmt.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Set Up Additional Binary Formats.
Jun 24 07:52:52 galelhiani systemd[1]: proc-sys-fs-binfmt_misc.automount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd-networkd[843]: enp0s1: DHCPv6 lease lost
Jun 24 07:52:52 galelhiani systemd[1]: Unset automount Arbitrary Executable File Formats File System Automount Point.
Jun 24 07:52:52 galelhiani systemd[1]: proc-sys-fs-binfmt_misc.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-timesyncd.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Network Time Synchronization.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-networkd.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Network Configuration.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-update-utmp.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Record System Boot/Shutdown in UTMP.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Preparation for Network.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-networkd.socket: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Closed Network Service Netlink Socket.
Jun 24 07:52:52 galelhiani systemd[1]: cloud-init-local.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Cloud-init: Local Stage (pre-network).
Jun 24 07:52:52 galelhiani systemd[1]: systemd-sysctl.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Apply Kernel Variables.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-modules-load.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Load Kernel Modules.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-tmpfiles-setup.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Create Volatile Files and Directories.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Local File Systems.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Mounted snaps.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /boot/efi...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /media/galelhiani/Ubuntu-Server 22.04.5 LTS arm64...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /run/credentials/systemd-sysusers.service...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /run/snapd/ns/lxd.mnt...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /run/snapd/ns/mesa-2404.mnt...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for bare, revision 5...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for core20, revision 2321...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for core20, revision 2870...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for core24, revision 1644...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for firefox, revision 8386...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for firefox, revision 8416...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for gnome-46-2404, revision 154...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for gtk-common-themes, revision 1535...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for lxd, revision 29353...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for lxd, revision 38801...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for mesa-2404, revision 1166...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for mesa-2404, revision 1778...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for snapd, revision 21761...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting Mount unit for snapd, revision 26869...
Jun 24 07:52:52 galelhiani systemd[1]: boot-efi.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /boot/efi.
Jun 24 07:52:52 galelhiani systemd[1]: media-galelhiani-Ubuntu\x2dServer\x2022.04.5\x20LTS\x20arm64.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /media/galelhiani/Ubuntu-Server 22.04.5 LTS arm64.
Jun 24 07:52:52 galelhiani systemd[1]: run-credentials-systemd\x2dsysusers.service.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /run/credentials/systemd-sysusers.service.
Jun 24 07:52:52 galelhiani systemd[1]: run-snapd-ns-lxd.mnt.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /run/snapd/ns/lxd.mnt.
Jun 24 07:52:52 galelhiani systemd[1]: run-snapd-ns-mesa\x2d2404.mnt.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /run/snapd/ns/mesa-2404.mnt.
Jun 24 07:52:52 galelhiani systemd[1]: snap-bare-5.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for bare, revision 5.
Jun 24 07:52:52 galelhiani systemd[1]: snap-core20-2321.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for core20, revision 2321.
Jun 24 07:52:52 galelhiani systemd[1]: snap-core20-2870.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for core20, revision 2870.
Jun 24 07:52:52 galelhiani systemd[1]: snap-core24-1644.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for core24, revision 1644.
Jun 24 07:52:52 galelhiani systemd[1]: snap-firefox-8386.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for firefox, revision 8386.
Jun 24 07:52:52 galelhiani systemd[1]: snap-firefox-8416.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for firefox, revision 8416.
Jun 24 07:52:52 galelhiani systemd[1]: snap-gnome\x2d46\x2d2404-154.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for gnome-46-2404, revision 154.
Jun 24 07:52:52 galelhiani systemd[1]: snap-gtk\x2dcommon\x2dthemes-1535.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for gtk-common-themes, revision 1535.
Jun 24 07:52:52 galelhiani systemd[1]: snap-lxd-29353.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for lxd, revision 29353.
Jun 24 07:52:52 galelhiani systemd[1]: snap-lxd-38801.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for lxd, revision 38801.
Jun 24 07:52:52 galelhiani systemd[1]: snap-mesa\x2d2404-1166.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for mesa-2404, revision 1166.
Jun 24 07:52:52 galelhiani systemd[1]: snap-mesa\x2d2404-1778.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for mesa-2404, revision 1778.
Jun 24 07:52:52 galelhiani systemd[1]: snap-snapd-21761.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for snapd, revision 21761.
Jun 24 07:52:52 galelhiani systemd[1]: snap-snapd-26869.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted Mount unit for snapd, revision 26869.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Mounting snaps.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /boot...
Jun 24 07:52:52 galelhiani systemd[1]: Unmounting /run/snapd/ns...
Jun 24 07:52:52 galelhiani systemd[1]: systemd-fsck@dev-disk-by\x2duuid-1B0A\x2d2B4E.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped File System Check on /dev/disk/by-uuid/1B0A-2B4E.
Jun 24 07:52:52 galelhiani systemd[1]: run-snapd-ns.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /run/snapd/ns.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Swaps.
Jun 24 07:52:52 galelhiani systemd[1]: Deactivating swap /swap.img...
Jun 24 07:52:52 galelhiani systemd[1]: swap.img.swap: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Deactivated swap /swap.img.
Jun 24 07:52:52 galelhiani systemd[1]: boot.mount: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Unmounted /boot.
Jun 24 07:52:52 galelhiani systemd[1]: Reached target Unmount All Filesystems.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-fsck@dev-disk-by\x2duuid-ee2146c8\x2d069d\x2d4b04\x2d9520\x2d7d50b84e6873.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped File System Check on /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873.
Jun 24 07:52:52 galelhiani systemd[1]: Removed slice Slice /system/systemd-fsck.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped target Preparation for Local File Systems.
Jun 24 07:52:52 galelhiani systemd[1]: Stopping Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling...
Jun 24 07:52:52 galelhiani multipathd[525]: exit (signal)
Jun 24 07:52:52 galelhiani multipathd[525]: --------shut down-------
Jun 24 07:52:52 galelhiani systemd[1]: Stopping Device-Mapper Multipath Device Controller...
Jun 24 07:52:52 galelhiani lvm[8540]:   1 logical volume(s) in volume group "ubuntu-vg" unmonitored
Jun 24 07:52:52 galelhiani systemd[1]: systemd-tmpfiles-setup-dev.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Create Static Device Nodes in /dev.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-sysusers.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Create System Users.
Jun 24 07:52:52 galelhiani systemd[1]: multipathd.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Device-Mapper Multipath Device Controller.
Jun 24 07:52:52 galelhiani systemd[1]: multipathd.service: Consumed 13.900s CPU time.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-remount-fs.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Remount Root and Kernel File Systems.
Jun 24 07:52:52 galelhiani systemd[1]: lvm2-monitor.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Stopped Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.
Jun 24 07:52:52 galelhiani systemd[1]: Reached target System Shutdown.
Jun 24 07:52:52 galelhiani systemd[1]: Reached target Late Shutdown Services.
Jun 24 07:52:52 galelhiani systemd[1]: systemd-poweroff.service: Deactivated successfully.
Jun 24 07:52:52 galelhiani systemd[1]: Finished System Power Off.
Jun 24 07:52:52 galelhiani systemd[1]: Reached target System Power Off.
Jun 24 07:52:52 galelhiani systemd[1]: Shutting down.
Jun 24 07:52:52 galelhiani systemd-shutdown[1]: Syncing filesystems and block devices.
Jun 24 07:52:52 galelhiani systemd-shutdown[1]: Sending SIGTERM to remaining processes...
Jun 24 07:52:52 galelhiani systemd-journald[485]: Journal stopped
-- Boot 560ba2114b614526b971946dc648055b --
Jun 24 07:53:40 galelhiani kernel: Booting Linux on physical CPU 0x0000000000 [0x610f0000]
Jun 24 07:53:40 galelhiani kernel: Linux version 5.15.0-181-generic (buildd@bos03-arm64-052) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #191-Ubuntu SMP Fri May 22 19:27:05 UTC 2026 (Ubuntu 5.15.0-181.191-generic 5.15.199)
Jun 24 07:53:40 galelhiani kernel: efi: EFI v2.70 by EDK II
Jun 24 07:53:40 galelhiani kernel: efi: ACPI 2.0=0x26fbf0018 SMBIOS=0xfffff000 SMBIOS 3.0=0x26fc19000 MOKvar=0x26fba0000 RNG=0x26fbffd18 MEMRESERVE=0x26dfcaf98 
Jun 24 07:53:40 galelhiani kernel: random: crng init done
Jun 24 07:53:40 galelhiani kernel: secureboot: Secure boot disabled
Jun 24 07:53:40 galelhiani kernel: ACPI: Early table checksum verification disabled
Jun 24 07:53:40 galelhiani kernel: ACPI: RSDP 0x000000026FBF0018 000024 (v02 APPLE )
Jun 24 07:53:40 galelhiani kernel: ACPI: XSDT 0x000000026FBFFE98 000044 (v01 APPLE  Apple Vz 00000001      01000013)
Jun 24 07:53:40 galelhiani kernel: ACPI: FACP 0x000000026FBFFA98 000114 (v06 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 07:53:40 galelhiani kernel: ACPI: DSDT 0x000000026FBFF698 0003CE (v02 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 07:53:40 galelhiani kernel: ACPI: GTDT 0x000000026FBFFC18 000068 (v03 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 07:53:40 galelhiani kernel: ACPI: APIC 0x000000026FBFE998 00024C (v05 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 07:53:40 galelhiani kernel: ACPI: MCFG 0x000000026FBFFF98 00003C (v01 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 07:53:40 galelhiani kernel: NUMA: Failed to initialise from firmware
Jun 24 07:53:40 galelhiani kernel: NUMA: Faking a node at [mem 0x0000000070000000-0x000000026fffffff]
Jun 24 07:53:40 galelhiani kernel: NUMA: NODE_DATA [mem 0x26ef16f80-0x26ef1bfff]
Jun 24 07:53:40 galelhiani kernel: Zone ranges:
Jun 24 07:53:40 galelhiani kernel:   DMA      [mem 0x0000000070000000-0x00000000ffffffff]
Jun 24 07:53:40 galelhiani kernel:   DMA32    empty
Jun 24 07:53:40 galelhiani kernel:   Normal   [mem 0x0000000100000000-0x000000026fffffff]
Jun 24 07:53:40 galelhiani kernel:   Device   empty
Jun 24 07:53:40 galelhiani kernel: Movable zone start for each node
Jun 24 07:53:40 galelhiani kernel: Early memory node ranges
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x0000000070000000-0x00000000ffffdfff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x00000000ffffe000-0x00000000ffffffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x0000000100000000-0x000000026e56ffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026e570000-0x000000026e6fffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026e700000-0x000000026fafffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026fb00000-0x000000026fb8ffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026fb90000-0x000000026fb9ffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026fba0000-0x000000026fbdffff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026fbe0000-0x000000026fc17fff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026fc18000-0x000000026fc19fff]
Jun 24 07:53:40 galelhiani kernel:   node   0: [mem 0x000000026fc1a000-0x000000026fffffff]
Jun 24 07:53:40 galelhiani kernel: Initmem setup node 0 [mem 0x0000000070000000-0x000000026fffffff]
Jun 24 07:53:40 galelhiani kernel: cma: Reserved 32 MiB at 0x00000000fd000000
Jun 24 07:53:40 galelhiani kernel: psci: probing for conduit method from ACPI.
Jun 24 07:53:40 galelhiani kernel: psci: PSCIv1.1 detected in firmware.
Jun 24 07:53:40 galelhiani kernel: psci: Using standard PSCI v0.2 function IDs
Jun 24 07:53:40 galelhiani kernel: psci: Trusted OS migration not required
Jun 24 07:53:40 galelhiani kernel: psci: SMC Calling Convention v1.1
Jun 24 07:53:40 galelhiani kernel: ACPI: SRAT not present
Jun 24 07:53:40 galelhiani kernel: percpu: Embedded 31 pages/cpu s88792 r8192 d29992 u126976
Jun 24 07:53:40 galelhiani kernel: pcpu-alloc: s88792 r8192 d29992 u126976 alloc=31*4096
Jun 24 07:53:40 galelhiani kernel: pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 [0] 4 [0] 5 
Jun 24 07:53:40 galelhiani kernel: Detected PIPT I-cache on CPU0
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Address authentication (IMP DEF algorithm)
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: GIC system register CPU interface
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Spectre-v4
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Spectre-BHB
Jun 24 07:53:40 galelhiani kernel: alternatives: patching kernel code
Jun 24 07:53:40 galelhiani kernel: Built 1 zonelists, mobility grouping on.  Total pages: 2064384
Jun 24 07:53:40 galelhiani kernel: Policy zone: Normal
Jun 24 07:53:40 galelhiani kernel: Kernel command line: BOOT_IMAGE=/vmlinuz-5.15.0-181-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro
Jun 24 07:53:40 galelhiani kernel: Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: mem auto-init: stack:off, heap alloc:on, heap free:off
Jun 24 07:53:40 galelhiani kernel: software IO TLB: mapped [mem 0x00000000f9000000-0x00000000fd000000] (64MB)
Jun 24 07:53:40 galelhiani kernel: Memory: 7975356K/8388608K available (17536K kernel code, 4602K rwdata, 14112K rodata, 9664K init, 1193K bss, 380484K reserved, 32768K cma-reserved)
Jun 24 07:53:40 galelhiani kernel: SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=6, Nodes=1
Jun 24 07:53:40 galelhiani kernel: ftrace: allocating 54682 entries in 214 pages
Jun 24 07:53:40 galelhiani kernel: ftrace: allocated 214 pages with 5 groups
Jun 24 07:53:40 galelhiani kernel: trace event string verifier disabled
Jun 24 07:53:40 galelhiani kernel: rcu: Hierarchical RCU implementation.
Jun 24 07:53:40 galelhiani kernel: rcu:         RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=6.
Jun 24 07:53:40 galelhiani kernel:         Rude variant of Tasks RCU enabled.
Jun 24 07:53:40 galelhiani kernel:         Tracing variant of Tasks RCU enabled.
Jun 24 07:53:40 galelhiani kernel: rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
Jun 24 07:53:40 galelhiani kernel: rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=6
Jun 24 07:53:40 galelhiani kernel: NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
Jun 24 07:53:40 galelhiani kernel: GICv3: GIC: Using split EOI/Deactivate mode
Jun 24 07:53:40 galelhiani kernel: GICv3: 988 SPIs implemented
Jun 24 07:53:40 galelhiani kernel: GICv3: 0 Extended SPIs implemented
Jun 24 07:53:40 galelhiani kernel: GICv3: Distributor has Range Selector support
Jun 24 07:53:40 galelhiani kernel: Root IRQ handler: gic_handle_irq
Jun 24 07:53:40 galelhiani kernel: GICv3: 16 PPIs implemented
Jun 24 07:53:40 galelhiani kernel: GICv3: CPU0: found redistributor 0 region 0:0x0000000010010000
Jun 24 07:53:40 galelhiani kernel: GICv2m: range[mem 0x1fff0000-0x1fff0fff], SPI[128:255]
Jun 24 07:53:40 galelhiani kernel: arch_timer: cp15 timer(s) running at 24.00MHz (phys).
Jun 24 07:53:40 galelhiani kernel: clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
Jun 24 07:53:40 galelhiani kernel: sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
Jun 24 07:53:40 galelhiani kernel: Console: colour dummy device 80x25
Jun 24 07:53:40 galelhiani kernel: printk: console [tty0] enabled
Jun 24 07:53:40 galelhiani kernel: ACPI: Core revision 20210730
Jun 24 07:53:40 galelhiani kernel: Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=96000)
Jun 24 07:53:40 galelhiani kernel: pid_max: default: 32768 minimum: 301
Jun 24 07:53:40 galelhiani kernel: LSM: Security Framework initializing
Jun 24 07:53:40 galelhiani kernel: landlock: Up and running.
Jun 24 07:53:40 galelhiani kernel: Yama: becoming mindful.
Jun 24 07:53:40 galelhiani kernel: AppArmor: AppArmor initialized
Jun 24 07:53:40 galelhiani kernel: Mount-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: ACPI PPTT: No PPTT table found, CPU and cache topology may be inaccurate
Jun 24 07:53:40 galelhiani kernel: rcu: Hierarchical SRCU implementation.
Jun 24 07:53:40 galelhiani kernel: Remapping and enabling EFI services.
Jun 24 07:53:40 galelhiani kernel: smp: Bringing up secondary CPUs ...
Jun 24 07:53:40 galelhiani kernel: Detected PIPT I-cache on CPU1
Jun 24 07:53:40 galelhiani kernel: GICv3: CPU1: found redistributor 1 region 0:0x0000000010030000
Jun 24 07:53:40 galelhiani kernel: CPU1: Booted secondary processor 0x0000000001 [0x610f0000]
Jun 24 07:53:40 galelhiani kernel: Detected PIPT I-cache on CPU2
Jun 24 07:53:40 galelhiani kernel: GICv3: CPU2: found redistributor 2 region 0:0x0000000010050000
Jun 24 07:53:40 galelhiani kernel: CPU2: Booted secondary processor 0x0000000002 [0x610f0000]
Jun 24 07:53:40 galelhiani kernel: Detected PIPT I-cache on CPU3
Jun 24 07:53:40 galelhiani kernel: GICv3: CPU3: found redistributor 3 region 0:0x0000000010070000
Jun 24 07:53:40 galelhiani kernel: CPU3: Booted secondary processor 0x0000000003 [0x610f0000]
Jun 24 07:53:40 galelhiani kernel: Detected PIPT I-cache on CPU4
Jun 24 07:53:40 galelhiani kernel: GICv3: CPU4: found redistributor 4 region 0:0x0000000010090000
Jun 24 07:53:40 galelhiani kernel: CPU4: Booted secondary processor 0x0000000004 [0x610f0000]
Jun 24 07:53:40 galelhiani kernel: Detected PIPT I-cache on CPU5
Jun 24 07:53:40 galelhiani kernel: GICv3: CPU5: found redistributor 5 region 0:0x00000000100b0000
Jun 24 07:53:40 galelhiani kernel: CPU5: Booted secondary processor 0x0000000005 [0x610f0000]
Jun 24 07:53:40 galelhiani kernel: smp: Brought up 1 node, 6 CPUs
Jun 24 07:53:40 galelhiani kernel: SMP: Total of 6 processors activated.
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Branch Target Identification
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: ARMv8.4 Translation Table Level
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Data cache clean to the PoU not required for I/D coherence
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Common not Private translations
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: CRC32 instructions
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Data cache clean to Point of Deep Persistence
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Data cache clean to Point of Persistence
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: E0PD
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Enhanced Privileged Access Never
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Generic authentication (IMP DEF algorithm)
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: RCpc load-acquire (LDAPR)
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: LSE atomic instructions
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Privileged Access Never
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: RAS Extension Support
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: Speculation barrier (SB)
Jun 24 07:53:40 galelhiani kernel: CPU features: detected: TLB range maintenance instructions
Jun 24 07:53:40 galelhiani kernel: CPU: All CPU(s) started at EL2
Jun 24 07:53:40 galelhiani kernel: devtmpfs: initialized
Jun 24 07:53:40 galelhiani kernel: setend instruction emulation is not supported on this system
Jun 24 07:53:40 galelhiani kernel: KASLR enabled
Jun 24 07:53:40 galelhiani kernel: clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
Jun 24 07:53:40 galelhiani kernel: futex hash table entries: 2048 (order: 5, 131072 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: pinctrl core: initialized pinctrl subsystem
Jun 24 07:53:40 galelhiani kernel: SMBIOS 3.3.0 present.
Jun 24 07:53:40 galelhiani kernel: DMI: Apple Inc. Apple Virtualization Generic Platform, BIOS 2103.100.6.0.0 04/18/2026
Jun 24 07:53:40 galelhiani kernel: NET: Registered PF_NETLINK/PF_ROUTE protocol family
Jun 24 07:53:40 galelhiani kernel: DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations
Jun 24 07:53:40 galelhiani kernel: DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
Jun 24 07:53:40 galelhiani kernel: DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
Jun 24 07:53:40 galelhiani kernel: audit: initializing netlink subsys (disabled)
Jun 24 07:53:40 galelhiani kernel: audit: type=2000 audit(0.020:1): state=initialized audit_enabled=0 res=1
Jun 24 07:53:40 galelhiani kernel: thermal_sys: Registered thermal governor 'fair_share'
Jun 24 07:53:40 galelhiani kernel: thermal_sys: Registered thermal governor 'bang_bang'
Jun 24 07:53:40 galelhiani kernel: thermal_sys: Registered thermal governor 'step_wise'
Jun 24 07:53:40 galelhiani kernel: thermal_sys: Registered thermal governor 'user_space'
Jun 24 07:53:40 galelhiani kernel: thermal_sys: Registered thermal governor 'power_allocator'
Jun 24 07:53:40 galelhiani kernel: cpuidle: using governor ladder
Jun 24 07:53:40 galelhiani kernel: cpuidle: using governor menu
Jun 24 07:53:40 galelhiani kernel: hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
Jun 24 07:53:40 galelhiani kernel: ASID allocator initialised with 65536 entries
Jun 24 07:53:40 galelhiani kernel: ACPI: bus type PCI registered
Jun 24 07:53:40 galelhiani kernel: acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
Jun 24 07:53:40 galelhiani kernel: Serial: AMBA PL011 UART driver
Jun 24 07:53:40 galelhiani kernel: HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
Jun 24 07:53:40 galelhiani kernel: HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
Jun 24 07:53:40 galelhiani kernel: HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
Jun 24 07:53:40 galelhiani kernel: HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
Jun 24 07:53:40 galelhiani kernel: fbcon: Taking over console
Jun 24 07:53:40 galelhiani kernel: ACPI: Added _OSI(Module Device)
Jun 24 07:53:40 galelhiani kernel: ACPI: Added _OSI(Processor Device)
Jun 24 07:53:40 galelhiani kernel: ACPI: Added _OSI(Processor Aggregator Device)
Jun 24 07:53:40 galelhiani kernel: ACPI: Added _OSI(Linux-Dell-Video)
Jun 24 07:53:40 galelhiani kernel: ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
Jun 24 07:53:40 galelhiani kernel: ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
Jun 24 07:53:40 galelhiani kernel: ACPI: 1 ACPI AML tables successfully acquired and loaded
Jun 24 07:53:40 galelhiani kernel: ACPI: Interpreter enabled
Jun 24 07:53:40 galelhiani kernel: ACPI: Using GIC for interrupt routing
Jun 24 07:53:40 galelhiani kernel: ACPI: MCFG table detected, 1 entries
Jun 24 07:53:40 galelhiani kernel: ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
Jun 24 07:53:40 galelhiani kernel: acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI EDR HPX-Type3]
Jun 24 07:53:40 galelhiani kernel: acpi PNP0A08:00: _OSC: platform retains control of PCIe features (AE_NOT_FOUND)
Jun 24 07:53:40 galelhiani kernel: acpi PNP0A08:00: ECAM area [mem 0x40000000-0x4fffffff] reserved by PNP0C02:00
Jun 24 07:53:40 galelhiani kernel: acpi PNP0A08:00: ECAM at [mem 0x40000000-0x4fffffff] for [bus 00-ff]
Jun 24 07:53:40 galelhiani kernel: ACPI: Remapped I/O 0x000000006fff0000 to [io  0x0000-0xffff window]
Jun 24 07:53:40 galelhiani kernel: PCI host bridge to bus 0000:00
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: root bus resource [mem 0x50000000-0x6ffdffff window]
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: root bus resource [mem 0x280000000-0x67fffffff window]
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: root bus resource [io  0x0000-0xffff window]
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: root bus resource [bus 00-ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:00.0: [106b:1a05] type 00 class 0x060000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:01.0: [1af4:1041] type 00 class 0x020000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:01.0: reg 0x10: [mem 0x280080000-0x28008ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:01.0: reg 0x18: [mem 0x5000d000-0x5000d03f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:05.0: [1af4:1042] type 00 class 0x018000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:05.0: reg 0x10: [mem 0x280070000-0x28007ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:05.0: reg 0x18: [mem 0x5000c000-0x5000c03f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:06.0: [1af4:105a] type 00 class 0x018000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:06.0: reg 0x10: [mem 0x280060000-0x28006ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:06.0: reg 0x18: [mem 0x5000b000-0x5000b03f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:07.0: [1af4:105a] type 00 class 0x018000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:07.0: reg 0x10: [mem 0x280050000-0x28005ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:07.0: reg 0x18: [mem 0x5000a000-0x5000a03f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:08.0: [1af4:1050] type 00 class 0x038000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:08.0: reg 0x10: [mem 0x280040000-0x28004ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:08.0: reg 0x18: [mem 0x50009000-0x5000903f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:09.0: [1af4:1059] type 00 class 0x040100
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:09.0: reg 0x10: [mem 0x280030000-0x28003ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:09.0: reg 0x18: [mem 0x50006000-0x5000607f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0a.0: [1af4:1059] type 00 class 0x040100
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0a.0: reg 0x10: [mem 0x280020000-0x28002ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0a.0: reg 0x18: [mem 0x50005000-0x5000507f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0b.0: [1af4:1044] type 00 class 0x100000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0b.0: reg 0x10: [mem 0x280090000-0x280097fff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0b.0: reg 0x18: [mem 0x50008000-0x5000803f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0c.0: [1af4:1045] type 00 class 0x058000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0c.0: reg 0x10: [mem 0x280010000-0x28001ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0c.0: reg 0x18: [mem 0x50007000-0x5000703f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0d.0: [1af4:1043] type 00 class 0x078000
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0d.0: reg 0x10: [mem 0x280000000-0x28000ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0d.0: reg 0x18: [mem 0x50004000-0x5000407f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0e.0: [106b:1a06] type 00 class 0x0c0330
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0e.0: reg 0x10: [mem 0x50003000-0x50003fff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0e.0: reg 0x14: [mem 0x50002000-0x500023ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0f.0: [106b:1a06] type 00 class 0x0c0330
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0f.0: reg 0x10: [mem 0x50001000-0x50001fff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0f.0: reg 0x14: [mem 0x50000000-0x500003ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:01.0: BAR 0: assigned [mem 0x280000000-0x28000ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:05.0: BAR 0: assigned [mem 0x280010000-0x28001ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:06.0: BAR 0: assigned [mem 0x280020000-0x28002ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:07.0: BAR 0: assigned [mem 0x280030000-0x28003ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:08.0: BAR 0: assigned [mem 0x280040000-0x28004ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:09.0: BAR 0: assigned [mem 0x280050000-0x28005ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0a.0: BAR 0: assigned [mem 0x280060000-0x28006ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0c.0: BAR 0: assigned [mem 0x280070000-0x28007ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0d.0: BAR 0: assigned [mem 0x280080000-0x28008ffff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0b.0: BAR 0: assigned [mem 0x280090000-0x280097fff 64bit]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0e.0: BAR 0: assigned [mem 0x50000000-0x50000fff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0f.0: BAR 0: assigned [mem 0x50001000-0x50001fff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0e.0: BAR 1: assigned [mem 0x50002000-0x500023ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0f.0: BAR 1: assigned [mem 0x50002400-0x500027ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:09.0: BAR 2: assigned [mem 0x50002800-0x5000287f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0a.0: BAR 2: assigned [mem 0x50002880-0x500028ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0d.0: BAR 2: assigned [mem 0x50002900-0x5000297f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:01.0: BAR 2: assigned [mem 0x50002980-0x500029bf]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:05.0: BAR 2: assigned [mem 0x500029c0-0x500029ff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:06.0: BAR 2: assigned [mem 0x50002a00-0x50002a3f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:07.0: BAR 2: assigned [mem 0x50002a40-0x50002a7f]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:08.0: BAR 2: assigned [mem 0x50002a80-0x50002abf]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0b.0: BAR 2: assigned [mem 0x50002ac0-0x50002aff]
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0c.0: BAR 2: assigned [mem 0x50002b00-0x50002b3f]
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: resource 4 [mem 0x50000000-0x6ffdffff window]
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: resource 5 [mem 0x280000000-0x67fffffff window]
Jun 24 07:53:40 galelhiani kernel: pci_bus 0000:00: resource 6 [io  0x0000-0xffff window]
Jun 24 07:53:40 galelhiani kernel: iommu: Default domain type: Translated 
Jun 24 07:53:40 galelhiani kernel: iommu: DMA domain TLB invalidation policy: strict mode 
Jun 24 07:53:40 galelhiani kernel: SCSI subsystem initialized
Jun 24 07:53:40 galelhiani kernel: libata version 3.00 loaded.
Jun 24 07:53:40 galelhiani kernel: vgaarb: loaded
Jun 24 07:53:40 galelhiani kernel: ACPI: bus type USB registered
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new interface driver usbfs
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new interface driver hub
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new device driver usb
Jun 24 07:53:40 galelhiani kernel: pps_core: LinuxPPS API ver. 1 registered
Jun 24 07:53:40 galelhiani kernel: pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
Jun 24 07:53:40 galelhiani kernel: PTP clock support registered
Jun 24 07:53:40 galelhiani kernel: EDAC MC: Ver: 3.0.0
Jun 24 07:53:40 galelhiani kernel: Registered efivars operations
Jun 24 07:53:40 galelhiani kernel: NetLabel: Initializing
Jun 24 07:53:40 galelhiani kernel: NetLabel:  domain hash size = 128
Jun 24 07:53:40 galelhiani kernel: NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
Jun 24 07:53:40 galelhiani kernel: NetLabel:  unlabeled traffic allowed by default
Jun 24 07:53:40 galelhiani kernel: clocksource: Switched to clocksource arch_sys_counter
Jun 24 07:53:40 galelhiani kernel: VFS: Disk quotas dquot_6.6.0
Jun 24 07:53:40 galelhiani kernel: VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
Jun 24 07:53:40 galelhiani kernel: AppArmor: AppArmor Filesystem Enabled
Jun 24 07:53:40 galelhiani kernel: pnp: PnP ACPI init
Jun 24 07:53:40 galelhiani kernel: system 00:00: [mem 0x40000000-0x4fffffff] could not be reserved
Jun 24 07:53:40 galelhiani kernel: pnp: PnP ACPI: found 1 devices
Jun 24 07:53:40 galelhiani kernel: NET: Registered PF_INET protocol family
Jun 24 07:53:40 galelhiani kernel: IP idents hash table entries: 131072 (order: 8, 1048576 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: TCP established hash table entries: 65536 (order: 7, 524288 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: TCP: Hash tables configured (established 65536 bind 65536)
Jun 24 07:53:40 galelhiani kernel: MPTCP token hash table entries: 8192 (order: 6, 196608 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: UDP hash table entries: 4096 (order: 5, 131072 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes, linear)
Jun 24 07:53:40 galelhiani kernel: NET: Registered PF_UNIX/PF_LOCAL protocol family
Jun 24 07:53:40 galelhiani kernel: NET: Registered PF_XDP protocol family
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0e.0: enabling device (0010 -> 0012)
Jun 24 07:53:40 galelhiani kernel: pci 0000:00:0f.0: enabling device (0010 -> 0012)
Jun 24 07:53:40 galelhiani kernel: PCI: CLS 0 bytes, default 64
Jun 24 07:53:40 galelhiani kernel: Trying to unpack rootfs image as initramfs...
Jun 24 07:53:40 galelhiani kernel: kvm [1]: IPA Size Limit: 40 bits
Jun 24 07:53:40 galelhiani kernel: kvm [1]: GICv3: no GICV resource entry
Jun 24 07:53:40 galelhiani kernel: kvm [1]: disabling GICv2 emulation
Jun 24 07:53:40 galelhiani kernel: kvm [1]: GIC system register CPU interface enabled
Jun 24 07:53:40 galelhiani kernel: kvm [1]: vgic interrupt IRQ9
Jun 24 07:53:40 galelhiani kernel: kvm [1]: Hyp mode initialized successfully
Jun 24 07:53:40 galelhiani kernel: Initialise system trusted keyrings
Jun 24 07:53:40 galelhiani kernel: Key type blacklist registered
Jun 24 07:53:40 galelhiani kernel: workingset: timestamp_bits=40 max_order=21 bucket_order=0
Jun 24 07:53:40 galelhiani kernel: zbud: loaded
Jun 24 07:53:40 galelhiani kernel: squashfs: version 4.0 (2009/01/31) Phillip Lougher
Jun 24 07:53:40 galelhiani kernel: fuse: init (API version 7.34)
Jun 24 07:53:40 galelhiani kernel: integrity: Platform Keyring initialized
Jun 24 07:53:40 galelhiani kernel: Key type asymmetric registered
Jun 24 07:53:40 galelhiani kernel: Asymmetric key parser 'x509' registered
Jun 24 07:53:40 galelhiani kernel: Block layer SCSI generic (bsg) driver version 0.4 loaded (major 242)
Jun 24 07:53:40 galelhiani kernel: io scheduler mq-deadline registered
Jun 24 07:53:40 galelhiani kernel: pl061_gpio ARMH0061:00: PL061 GPIO chip registered
Jun 24 07:53:40 galelhiani kernel: shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
Jun 24 07:53:40 galelhiani kernel: input: Power Button as /devices/LNXSYSTM:00/PNP0C0C:00/input/input0
Jun 24 07:53:40 galelhiani kernel: ACPI: button: Power Button [PWRB]
Jun 24 07:53:40 galelhiani kernel: Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
Jun 24 07:53:40 galelhiani kernel: SuperH (H)SCI(F) driver initialized
Jun 24 07:53:40 galelhiani kernel: msm_serial: driver initialized
Jun 24 07:53:40 galelhiani kernel: cacheinfo: Unable to detect cache hierarchy for CPU 0
Jun 24 07:53:40 galelhiani kernel: loop: module loaded
Jun 24 07:53:40 galelhiani kernel: SPI driver altr_a10sr has no spi_device_id for altr,a10sr
Jun 24 07:53:40 galelhiani kernel: tun: Universal TUN/TAP device driver, 1.6
Jun 24 07:53:40 galelhiani kernel: PPP generic driver version 2.4.2
Jun 24 07:53:40 galelhiani kernel: ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
Jun 24 07:53:40 galelhiani kernel: ehci-pci: EHCI PCI platform driver
Jun 24 07:53:40 galelhiani kernel: ehci-orion: EHCI orion driver
Jun 24 07:53:40 galelhiani kernel: ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
Jun 24 07:53:40 galelhiani kernel: ohci-pci: OHCI PCI platform driver
Jun 24 07:53:40 galelhiani kernel: uhci_hcd: USB Universal Host Controller Interface driver
Jun 24 07:53:40 galelhiani kernel: mousedev: PS/2 mouse device common for all mice
Jun 24 07:53:40 galelhiani kernel: rtc-efi rtc-efi.0: registered as rtc0
Jun 24 07:53:40 galelhiani kernel: rtc-efi rtc-efi.0: setting system clock to 2026-06-24T07:53:38 UTC (1782287618)
Jun 24 07:53:40 galelhiani kernel: i2c_dev: i2c /dev entries driver
Jun 24 07:53:40 galelhiani kernel: device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
Jun 24 07:53:40 galelhiani kernel: device-mapper: uevent: version 1.0.3
Jun 24 07:53:40 galelhiani kernel: device-mapper: ioctl: 4.45.0-ioctl (2021-03-22) initialised: dm-devel@redhat.com
Jun 24 07:53:40 galelhiani kernel: ledtrig-cpu: registered to indicate activity on CPUs
Jun 24 07:53:40 galelhiani kernel: drop_monitor: Initializing network drop monitor service
Jun 24 07:53:40 galelhiani kernel: NET: Registered PF_INET6 protocol family
Jun 24 07:53:40 galelhiani kernel: Freeing initrd memory: 103836K
Jun 24 07:53:40 galelhiani kernel: Segment Routing with IPv6
Jun 24 07:53:40 galelhiani kernel: In-situ OAM (IOAM) with IPv6
Jun 24 07:53:40 galelhiani kernel: NET: Registered PF_PACKET protocol family
Jun 24 07:53:40 galelhiani kernel: Key type dns_resolver registered
Jun 24 07:53:40 galelhiani kernel: registered taskstats version 1
Jun 24 07:53:40 galelhiani kernel: Loading compiled-in X.509 certificates
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Build time autogenerated kernel key: a112623dda86549bada95b36cd50fc4d89454411'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Live Patch Signing 2025 Kmod: d541cef61dc7e793b7eb7e899970a2eef0b5dc8c'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing 2025 Kmod: 4627603d2357a2a3f81006370894c221175893e9'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
Jun 24 07:53:40 galelhiani kernel: blacklist: Loading compiled-in revocation X.509 certificates
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing: 61482aa2830d0ab2ad5af10b7250da9033ddcef0'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2017): 242ade75ac4a15e50d50c84b0d45ff3eae707a03'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (ESM 2018): 365188c1d374d6b07c3c8f240f8ef722433d6a8b'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2019): c0746fd6c5da3ae827864651ad66ae47fe24b3e8'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v1): a8d54bbb3825cfb94fa13c9f8a594a195c107b8d'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v2): 4cf046892d6fd3c9a5b03f98d845f90851dc6a8c'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af'
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (Ubuntu Core 2019): c1d57b8f6b743f23ee41f4f7ee292f06eecadfb9'
Jun 24 07:53:40 galelhiani kernel: zswap: loaded using pool lzo/zbud
Jun 24 07:53:40 galelhiani kernel: Key type .fscrypt registered
Jun 24 07:53:40 galelhiani kernel: Key type fscrypt-provisioning registered
Jun 24 07:53:40 galelhiani kernel: cryptd: max_cpu_qlen set to 1000
Jun 24 07:53:40 galelhiani kernel: Key type encrypted registered
Jun 24 07:53:40 galelhiani kernel: AppArmor: AppArmor sha1 policy hashing enabled
Jun 24 07:53:40 galelhiani kernel: integrity: Loading X.509 certificate: UEFI:MokListRT (MOKvar table)
Jun 24 07:53:40 galelhiani kernel: integrity: Loaded X.509 cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63'
Jun 24 07:53:40 galelhiani kernel: ima: No TPM chip found, activating TPM-bypass!
Jun 24 07:53:40 galelhiani kernel: Loading compiled-in module X.509 certificates
Jun 24 07:53:40 galelhiani kernel: Loaded X.509 cert 'Build time autogenerated kernel key: a112623dda86549bada95b36cd50fc4d89454411'
Jun 24 07:53:40 galelhiani kernel: ima: Allocated hash algorithm: sha1
Jun 24 07:53:40 galelhiani kernel: ima: No architecture policies found
Jun 24 07:53:40 galelhiani kernel: evm: Initialising EVM extended attributes:
Jun 24 07:53:40 galelhiani kernel: evm: security.selinux
Jun 24 07:53:40 galelhiani kernel: evm: security.SMACK64
Jun 24 07:53:40 galelhiani kernel: evm: security.SMACK64EXEC
Jun 24 07:53:40 galelhiani kernel: evm: security.SMACK64TRANSMUTE
Jun 24 07:53:40 galelhiani kernel: evm: security.SMACK64MMAP
Jun 24 07:53:40 galelhiani kernel: evm: security.apparmor
Jun 24 07:53:40 galelhiani kernel: evm: security.ima
Jun 24 07:53:40 galelhiani kernel: evm: security.capability
Jun 24 07:53:40 galelhiani kernel: evm: HMAC attrs: 0x1
Jun 24 07:53:40 galelhiani kernel: clk: Disabling unused clocks
Jun 24 07:53:40 galelhiani kernel: Freeing unused kernel memory: 9664K
Jun 24 07:53:40 galelhiani kernel: Checked W+X mappings: passed, no W+X pages found
Jun 24 07:53:40 galelhiani kernel: Run /init as init process
Jun 24 07:53:40 galelhiani kernel:   with arguments:
Jun 24 07:53:40 galelhiani kernel:     /init
Jun 24 07:53:40 galelhiani kernel:   with environment:
Jun 24 07:53:40 galelhiani kernel:     HOME=/
Jun 24 07:53:40 galelhiani kernel:     TERM=linux
Jun 24 07:53:40 galelhiani kernel: virtio_blk virtio1: [vda] 209715200 512-byte logical blocks (107 GB/100 GiB)
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0e.0: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0e.0: new USB bus registered, assigned bus number 1
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0e.0: hcc params 0x02600801 hci version 0x110 quirks 0x0000000000000010
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0e.0: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0e.0: new USB bus registered, assigned bus number 2
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0e.0: Host supports USB 3.1 Enhanced SuperSpeed
Jun 24 07:53:40 galelhiani kernel: usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
Jun 24 07:53:40 galelhiani kernel: usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 07:53:40 galelhiani kernel: usb usb1: Product: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: usb usb1: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 07:53:40 galelhiani kernel: usb usb1: SerialNumber: 0000:00:0e.0
Jun 24 07:53:40 galelhiani kernel: hub 1-0:1.0: USB hub found
Jun 24 07:53:40 galelhiani kernel: hub 1-0:1.0: 8 ports detected
Jun 24 07:53:40 galelhiani kernel: usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
Jun 24 07:53:40 galelhiani kernel: usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
Jun 24 07:53:40 galelhiani kernel: usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 07:53:40 galelhiani kernel: usb usb2: Product: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: usb usb2: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 07:53:40 galelhiani kernel: usb usb2: SerialNumber: 0000:00:0e.0
Jun 24 07:53:40 galelhiani kernel: hub 2-0:1.0: USB hub found
Jun 24 07:53:40 galelhiani kernel: hub 2-0:1.0: 8 ports detected
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0f.0: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0f.0: new USB bus registered, assigned bus number 3
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0f.0: hcc params 0x02600801 hci version 0x110 quirks 0x0000000000000010
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0f.0: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0f.0: new USB bus registered, assigned bus number 4
Jun 24 07:53:40 galelhiani kernel: xhci_hcd 0000:00:0f.0: Host supports USB 3.1 Enhanced SuperSpeed
Jun 24 07:53:40 galelhiani kernel: usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
Jun 24 07:53:40 galelhiani kernel: usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 07:53:40 galelhiani kernel: usb usb3: Product: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: usb usb3: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 07:53:40 galelhiani kernel: usb usb3: SerialNumber: 0000:00:0f.0
Jun 24 07:53:40 galelhiani kernel: hub 3-0:1.0: USB hub found
Jun 24 07:53:40 galelhiani kernel: hub 3-0:1.0: 8 ports detected
Jun 24 07:53:40 galelhiani kernel: usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
Jun 24 07:53:40 galelhiani kernel: usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
Jun 24 07:53:40 galelhiani kernel: usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 07:53:40 galelhiani kernel: usb usb4: Product: xHCI Host Controller
Jun 24 07:53:40 galelhiani kernel: usb usb4: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 07:53:40 galelhiani kernel: usb usb4: SerialNumber: 0000:00:0f.0
Jun 24 07:53:40 galelhiani kernel: hub 4-0:1.0: USB hub found
Jun 24 07:53:40 galelhiani kernel: hub 4-0:1.0: 8 ports detected
Jun 24 07:53:40 galelhiani kernel:  vda: vda1 vda2 vda3
Jun 24 07:53:40 galelhiani kernel: [drm] pci: virtio-gpu-pci detected at 0000:00:08.0
Jun 24 07:53:40 galelhiani kernel: [drm] features: -virgl -edid -resource_blob -host_visible
Jun 24 07:53:40 galelhiani kernel: [drm] number of scanouts: 1
Jun 24 07:53:40 galelhiani kernel: [drm] number of cap sets: 0
Jun 24 07:53:40 galelhiani kernel: [drm] Initialized virtio_gpu 0.1.0 0 for virtio4 on minor 0
Jun 24 07:53:40 galelhiani kernel: virtio_gpu virtio4: [drm] drm_plane_enable_fb_damage_clips() not called
Jun 24 07:53:40 galelhiani kernel: Console: switching to colour frame buffer device 200x79
Jun 24 07:53:40 galelhiani kernel: virtio_gpu virtio4: [drm] fb0: virtio_gpudrmfb frame buffer device
Jun 24 07:53:40 galelhiani kernel: virtio_net virtio0 enp0s1: renamed from eth0
Jun 24 07:53:40 galelhiani kernel: usb 1-1: new full-speed USB device number 2 using xhci_hcd
Jun 24 07:53:40 galelhiani kernel: usb 4-1: new SuperSpeed USB device number 2 using xhci_hcd
Jun 24 07:53:40 galelhiani kernel: usb 4-1: New USB device found, idVendor=05ac, idProduct=1503, bcdDevice= 0.00
Jun 24 07:53:40 galelhiani kernel: usb 4-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Jun 24 07:53:40 galelhiani kernel: usb 4-1: Product: Virtual USB Mass Storage Device
Jun 24 07:53:40 galelhiani kernel: usb 4-1: Manufacturer: Apple Inc.
Jun 24 07:53:40 galelhiani kernel: usb-storage 4-1:1.0: USB Mass Storage device detected
Jun 24 07:53:40 galelhiani kernel: scsi host0: usb-storage 4-1:1.0
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new interface driver usb-storage
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new interface driver uas
Jun 24 07:53:40 galelhiani kernel: raid6: neonx8   gen() 44709 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: neonx8   xor() 44256 MB/s
Jun 24 07:53:40 galelhiani kernel: usb 1-1: New USB device found, idVendor=05ac, idProduct=8105, bcdDevice= 0.00
Jun 24 07:53:40 galelhiani kernel: usb 1-1: New USB device strings: Mfr=2, Product=3, SerialNumber=0
Jun 24 07:53:40 galelhiani kernel: usb 1-1: Product: Virtual USB Keyboard
Jun 24 07:53:40 galelhiani kernel: usb 1-1: Manufacturer: Apple Inc.
Jun 24 07:53:40 galelhiani kernel: raid6: neonx4   gen() 51566 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: neonx4   xor() 44641 MB/s
Jun 24 07:53:40 galelhiani kernel: usb 1-2: new full-speed USB device number 3 using xhci_hcd
Jun 24 07:53:40 galelhiani kernel: raid6: neonx2   gen() 52396 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: neonx2   xor() 44419 MB/s
Jun 24 07:53:40 galelhiani kernel: usb 1-2: New USB device found, idVendor=05ac, idProduct=8106, bcdDevice= 0.00
Jun 24 07:53:40 galelhiani kernel: usb 1-2: New USB device strings: Mfr=2, Product=3, SerialNumber=0
Jun 24 07:53:40 galelhiani kernel: usb 1-2: Product: Virtual USB Digitizer
Jun 24 07:53:40 galelhiani kernel: usb 1-2: Manufacturer: Apple Inc.
Jun 24 07:53:40 galelhiani kernel: hid: raw HID events driver (C) Jiri Kosina
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new interface driver usbhid
Jun 24 07:53:40 galelhiani kernel: usbhid: USB HID core driver
Jun 24 07:53:40 galelhiani kernel: input: Apple Inc. Virtual USB Keyboard as /devices/pci0000:00/0000:00:0e.0/usb1/1-1/1-1:1.0/0003:05AC:8105.0001/input/input1
Jun 24 07:53:40 galelhiani kernel: raid6: neonx1   gen() 52316 MB/s
Jun 24 07:53:40 galelhiani kernel: hid-generic 0003:05AC:8105.0001: input,hidraw0: USB HID v1.10 Keyboard [Apple Inc. Virtual USB Keyboard] on usb-0000:00:0e.0-1/input0
Jun 24 07:53:40 galelhiani kernel: input: Apple Inc. Virtual USB Digitizer as /devices/pci0000:00/0000:00:0e.0/usb1/1-2/1-2:1.0/0003:05AC:8106.0002/input/input2
Jun 24 07:53:40 galelhiani kernel: hid-generic 0003:05AC:8106.0002: input,hidraw1: USB HID v1.10 Mouse [Apple Inc. Virtual USB Digitizer] on usb-0000:00:0e.0-2/input0
Jun 24 07:53:40 galelhiani kernel: raid6: neonx1   xor() 39599 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x8  gen() 25322 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x8  xor() 13785 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x4  gen() 23329 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x4  xor() 12763 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x2  gen() 20367 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x2  xor() 10798 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: int64x1  gen() 17803 MB/s
Jun 24 07:53:40 galelhiani kernel: scsi 0:0:0:0: Direct-Access     Apple    Virtual Disk     1    PQ: 0 ANSI: 6
Jun 24 07:53:40 galelhiani kernel: sd 0:0:0:0: Attached scsi generic sg0 type 0
Jun 24 07:53:40 galelhiani kernel: sd 0:0:0:0: [sda] 4027128 512-byte logical blocks: (2.06 GB/1.92 GiB)
Jun 24 07:53:40 galelhiani kernel: sd 0:0:0:0: [sda] Write Protect is on
Jun 24 07:53:40 galelhiani kernel: sd 0:0:0:0: [sda] Mode Sense: 21 00 80 00
Jun 24 07:53:40 galelhiani kernel: sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
Jun 24 07:53:40 galelhiani kernel:  sda: sda1 sda2
Jun 24 07:53:40 galelhiani kernel: sd 0:0:0:0: [sda] Attached SCSI disk
Jun 24 07:53:40 galelhiani kernel: raid6: int64x1  xor()  9073 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: using algorithm neonx2 gen() 52396 MB/s
Jun 24 07:53:40 galelhiani kernel: raid6: .... xor() 44419 MB/s, rmw enabled
Jun 24 07:53:40 galelhiani kernel: raid6: using neon recovery algorithm
Jun 24 07:53:40 galelhiani kernel: xor: measuring software checksum speed
Jun 24 07:53:40 galelhiani kernel:    8regs           : 52319 MB/sec
Jun 24 07:53:40 galelhiani kernel:    32regs          : 56283 MB/sec
Jun 24 07:53:40 galelhiani kernel:    arm64_neon      : 82453 MB/sec
Jun 24 07:53:40 galelhiani kernel: xor: using function: arm64_neon (82453 MB/sec)
Jun 24 07:53:40 galelhiani kernel: async_tx: api initialized (async)
Jun 24 07:53:40 galelhiani kernel: Btrfs loaded, crc32c=crc32c-generic, zoned=yes, fsverity=yes
Jun 24 07:53:40 galelhiani kernel: EXT4-fs (dm-0): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
Jun 24 07:53:40 galelhiani systemd[1]: Inserted module 'autofs4'
Jun 24 07:53:40 galelhiani systemd[1]: systemd 249.11-0ubuntu3.21 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
Jun 24 07:53:40 galelhiani systemd[1]: Detected architecture arm64.
Jun 24 07:53:40 galelhiani systemd[1]: Hostname set to <galelhiani>.
Jun 24 07:53:40 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 07:53:40 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 07:53:40 galelhiani systemd[1]: Queued start job for default target Graphical Interface.
Jun 24 07:53:40 galelhiani systemd[1]: Created slice Slice /system/modprobe.
Jun 24 07:53:40 galelhiani systemd[1]: Created slice Slice /system/systemd-fsck.
Jun 24 07:53:40 galelhiani systemd[1]: Created slice User and Session Slice.
Jun 24 07:53:40 galelhiani systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Jun 24 07:53:40 galelhiani systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Slice Units.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Mounting snaps.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Local Verity Protected Volumes.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Device-mapper event daemon FIFOs.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on LVM2 poll daemon socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on multipathd control socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Syslog Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on fsck to fsckd communication Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on initctl Compatibility Named Pipe.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Journal Audit Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Journal Socket (/dev/log).
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Journal Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Network Service Netlink Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on udev Control Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Listening on udev Kernel Socket.
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Huge Pages File System...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting POSIX Message Queue File System...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Kernel Debug File System...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Kernel Trace File System...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Journal Service...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Set the console keyboard layout...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Create List of Static Device Nodes...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling...
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in LXD - agent being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load Kernel Module configfs...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load Kernel Module drm...
Jun 24 07:53:40 galelhiani systemd-journald[478]: Journal started
Jun 24 07:53:40 galelhiani systemd-journald[478]: Runtime Journal (/run/log/journal/1955aac654704d37a292a15c85e64c9d) is 8.0M, max 79.3M, 71.3M free.
Jun 24 07:53:40 galelhiani lvm[483]:   1 logical volume(s) in volume group "ubuntu-vg" monitored
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load Kernel Module fuse...
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in OpenVSwitch configuration for cleanup being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
Jun 24 07:53:40 galelhiani kernel: pstore: Using crash dump compression: deflate
Jun 24 07:53:40 galelhiani kernel: pstore: Registered efi as persistent store backend
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load Kernel Modules...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Remount Root and Kernel File Systems...
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Huge Pages File System.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted POSIX Message Queue File System.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Kernel Debug File System.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Kernel Trace File System.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Create List of Static Device Nodes.
Jun 24 07:53:40 galelhiani systemd[1]: modprobe@configfs.service: Deactivated successfully.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load Kernel Module configfs.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Coldplug All udev Devices...
Jun 24 07:53:40 galelhiani systemd[1]: Started Journal Service.
Jun 24 07:53:40 galelhiani kernel: EXT4-fs (dm-0): re-mounted. Opts: (null). Quota mode: none.
Jun 24 07:53:40 galelhiani systemd[1]: modprobe@drm.service: Deactivated successfully.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load Kernel Module drm.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Set the console keyboard layout.
Jun 24 07:53:40 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 07:53:40 galelhiani systemd[1]: modprobe@fuse.service: Deactivated successfully.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load Kernel Module fuse.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load Kernel Modules.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Remount Root and Kernel File Systems.
Jun 24 07:53:40 galelhiani systemd[1]: Activating swap /swap.img...
Jun 24 07:53:40 galelhiani kernel: Adding 4194300k swap on /swap.img.  Priority:-2 extents:3 across:4464636k FS
Jun 24 07:53:40 galelhiani systemd[1]: Mounting FUSE Control File System...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Kernel Configuration File System...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Device-Mapper Multipath Device Controller...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Flush Journal to Persistent Storage...
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load/Save Random Seed...
Jun 24 07:53:40 galelhiani systemd-journald[478]: Time spent on flushing to /var/log/journal/1955aac654704d37a292a15c85e64c9d is 32.175ms for 576 entries.
Jun 24 07:53:40 galelhiani systemd-journald[478]: System Journal (/var/log/journal/1955aac654704d37a292a15c85e64c9d) is 128.0M, max 4.0G, 3.8G free.
Jun 24 07:53:40 galelhiani kernel: alua: device handler registered
Jun 24 07:53:40 galelhiani kernel: emc: device handler registered
Jun 24 07:53:40 galelhiani kernel: rdac: device handler registered
Jun 24 07:53:40 galelhiani kernel: loop0: detected capacity change from 0 to 8
Jun 24 07:53:40 galelhiani kernel: loop1: detected capacity change from 0 to 122368
Jun 24 07:53:40 galelhiani kernel: loop2: detected capacity change from 0 to 122008
Jun 24 07:53:40 galelhiani systemd[1]: Starting Apply Kernel Variables...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Create System Users...
Jun 24 07:53:40 galelhiani systemd[1]: Activated swap /swap.img.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Coldplug All udev Devices.
Jun 24 07:53:40 galelhiani multipathd[516]: --------start up--------
Jun 24 07:53:40 galelhiani multipathd[516]: read /etc/multipath.conf
Jun 24 07:53:40 galelhiani multipathd[516]: path checkers start up
Jun 24 07:53:40 galelhiani systemd[1]: Finished Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted FUSE Control File System.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Kernel Configuration File System.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load/Save Random Seed.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Apply Kernel Variables.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in First Boot Complete being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Swaps.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Create System Users.
Jun 24 07:53:40 galelhiani systemd[1]: Started Device-Mapper Multipath Device Controller.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Create Static Device Nodes in /dev...
Jun 24 07:53:40 galelhiani systemd[1]: Finished Create Static Device Nodes in /dev.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Preparation for Local File Systems.
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for bare, revision 5...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for core20, revision 2321...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for core20, revision 2870...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for core24, revision 1644...
Jun 24 07:53:40 galelhiani kernel: loop3: detected capacity change from 0 to 126688
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for firefox, revision 8386...
Jun 24 07:53:40 galelhiani kernel: loop4: detected capacity change from 0 to 483496
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for firefox, revision 8416...
Jun 24 07:53:40 galelhiani kernel: loop5: detected capacity change from 0 to 483616
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for gnome-46-2404, revision 154...
Jun 24 07:53:40 galelhiani kernel: loop6: detected capacity change from 0 to 1132440
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for gtk-common-themes, revision 1535...
Jun 24 07:53:40 galelhiani kernel: loop7: detected capacity change from 0 to 187776
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for lxd, revision 29353...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for lxd, revision 38801...
Jun 24 07:53:40 galelhiani kernel: loop8: detected capacity change from 0 to 158472
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for mesa-2404, revision 1166...
Jun 24 07:53:40 galelhiani kernel: loop9: detected capacity change from 0 to 165832
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for mesa-2404, revision 1778...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for snapd, revision 21761...
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Mount unit for snapd, revision 26869...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Rule-based Manager for Device Events and Files...
Jun 24 07:53:40 galelhiani systemd[1]: Finished Flush Journal to Persistent Storage.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for bare, revision 5.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for core20, revision 2321.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for core20, revision 2870.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for core24, revision 1644.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for firefox, revision 8386.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for firefox, revision 8416.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for gnome-46-2404, revision 154.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for gtk-common-themes, revision 1535.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for lxd, revision 29353.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for lxd, revision 38801.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for mesa-2404, revision 1166.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for mesa-2404, revision 1778.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for snapd, revision 21761.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted Mount unit for snapd, revision 26869.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Mounted snaps.
Jun 24 07:53:40 galelhiani systemd[1]: Started Rule-based Manager for Device Events and Files.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Local Encrypted Volumes.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in OpenVSwitch configuration for cleanup being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 07:53:40 galelhiani mtp-probe[582]: checking bus 4, device 2: "/sys/devices/pci0000:00/0000:00:0f.0/usb4/4-1"
Jun 24 07:53:40 galelhiani mtp-probe[583]: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:0e.0/usb1/1-2"
Jun 24 07:53:40 galelhiani systemd-udevd[564]: Using default interface naming scheme 'v249'.
Jun 24 07:53:40 galelhiani mtp-probe[582]: bus: 4, device: 2 was not an MTP device
Jun 24 07:53:40 galelhiani mtp-probe[583]: bus: 1, device: 3 was not an MTP device
Jun 24 07:53:40 galelhiani systemd[1]: Created slice Slice /system/lvm2-pvscan.
Jun 24 07:53:40 galelhiani systemd[1]: Starting LVM event activation on device 252:3...
Jun 24 07:53:40 galelhiani mtp-probe[587]: checking bus 1, device 2: "/sys/devices/pci0000:00/0000:00:0e.0/usb1/1-1"
Jun 24 07:53:40 galelhiani systemd[1]: Found device /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873.
Jun 24 07:53:40 galelhiani mtp-probe[587]: bus: 1, device: 2 was not an MTP device
Jun 24 07:53:40 galelhiani kernel: usbcore: registered new device driver apple-mfi-fastcharge
Jun 24 07:53:40 galelhiani systemd[1]: Found device /dev/disk/by-uuid/1B0A-2B4E.
Jun 24 07:53:40 galelhiani lvm[588]:   pvscan[588] PV /dev/vda3 online, VG ubuntu-vg is complete.
Jun 24 07:53:40 galelhiani lvm[588]:   pvscan[588] VG ubuntu-vg skip autoactivation.
Jun 24 07:53:40 galelhiani systemd[1]: Starting File System Check on /dev/disk/by-uuid/1B0A-2B4E...
Jun 24 07:53:40 galelhiani systemd[1]: Starting File System Check on /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873...
Jun 24 07:53:40 galelhiani systemd[1]: Started File System Check Daemon to report status.
Jun 24 07:53:40 galelhiani systemd-fsck[601]: fsck.fat 4.2 (2021-01-31)
Jun 24 07:53:40 galelhiani systemd-fsck[601]: /dev/vda1: 11 files, 1617/274658 clusters
Jun 24 07:53:40 galelhiani systemd[1]: Finished File System Check on /dev/disk/by-uuid/1B0A-2B4E.
Jun 24 07:53:40 galelhiani kernel: virtiofs virtio2: virtio_fs_setup_dax: No cache capability
Jun 24 07:53:40 galelhiani systemd-fsck[609]: /dev/vda2: clean, 260/131072 files, 91148/524288 blocks
Jun 24 07:53:40 galelhiani kernel: virtiofs virtio3: virtio_fs_setup_dax: No cache capability
Jun 24 07:53:40 galelhiani systemd[1]: Finished File System Check on /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873.
Jun 24 07:53:40 galelhiani systemd[1]: Mounting /boot...
Jun 24 07:53:40 galelhiani kernel: EXT4-fs (vda2): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted /boot.
Jun 24 07:53:40 galelhiani systemd[1]: Mounting /boot/efi...
Jun 24 07:53:40 galelhiani systemd[1]: Finished LVM event activation on device 252:3.
Jun 24 07:53:40 galelhiani systemd[1]: Mounted /boot/efi.
Jun 24 07:53:40 galelhiani systemd[1]: Reached target Local File Systems.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Load AppArmor profiles...
Jun 24 07:53:40 galelhiani apparmor.systemd[644]: Restarting AppArmor
Jun 24 07:53:40 galelhiani apparmor.systemd[644]: Reloading AppArmor profiles
Jun 24 07:53:40 galelhiani systemd[1]: Starting Set console font and keymap...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Create final runtime dir for shutdown pivot root...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Tell Plymouth To Write Out Runtime Data...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Set Up Additional Binary Formats...
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 24 07:53:40 galelhiani systemd[1]: Starting Create Volatile Files and Directories...
Jun 24 07:53:40 galelhiani systemd[1]: Starting Uncomplicated firewall...
Jun 24 07:53:40 galelhiani audit[671]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=671 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[671]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=671 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.944:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=671 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.944:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=671 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.948:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=669 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[669]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=669 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[672]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[672]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[672]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[672]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/{,usr/}sbin/dhclient" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani systemd[1]: Finished Set console font and keymap.
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.952:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.952:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.952:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.952:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/{,usr/}sbin/dhclient" pid=672 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.952:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="tcpdump" pid=685 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani kernel: audit: type=1400 audit(1782287620.952:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=684 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[685]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="tcpdump" pid=685 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[684]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=684 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[684]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=684 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[684]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=684 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani systemd[1]: Finished Create final runtime dir for shutdown pivot root.
Jun 24 07:53:40 galelhiani audit[673]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_apt_news" pid=673 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[690]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=690 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani systemd[1]: Finished Tell Plymouth To Write Out Runtime Data.
Jun 24 07:53:40 galelhiani systemd[1]: Finished Uncomplicated firewall.
Jun 24 07:53:40 galelhiani audit[686]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oosplash" pid=686 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani systemd[1]: Finished Create Volatile Files and Directories.
Jun 24 07:53:40 galelhiani audit[687]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=687 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//apt_methods" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//apt_methods_gpgv" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//cloud_id" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//dpkg" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//ps" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//ubuntu_distro_info" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache_systemctl" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[674]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache_systemd_detect_virt" pid=674 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani apparmor.systemd[695]: Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
Jun 24 07:53:40 galelhiani apparmor.systemd[696]: Warning: found usr.sbin.sssd in /etc/apparmor.d/force-complain, forcing complain mode
Jun 24 07:53:40 galelhiani systemd[1]: proc-sys-fs-binfmt_misc.automount: Got automount request for /proc/sys/fs/binfmt_misc, triggered by 665 (systemd-binfmt)
Jun 24 07:53:40 galelhiani audit[691]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=691 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[693]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=693 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[694]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/cups/backend/cups-pdf" pid=694 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[694]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cupsd" pid=694 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[694]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cupsd//third_party" pid=694 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani systemd[1]: Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
Jun 24 07:53:40 galelhiani systemd[1]: Mounting Arbitrary Executable File Formats File System...
Jun 24 07:53:40 galelhiani audit[675]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=675 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[675]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=675 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[675]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//snap_browsers" pid=675 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[675]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer" pid=675 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[675]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer//sanitized_helper" pid=675 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[675]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-thumbnailer" pid=675 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani audit[696]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/sssd" pid=696 comm="apparmor_parser"
Jun 24 07:53:40 galelhiani apparmor.systemd[696]: Warning from /etc/apparmor.d (/etc/apparmor.d/usr.sbin.sssd line 69): Caching disabled for: 'usr.sbin.sssd' due to force complain
Jun 24 07:53:41 galelhiani audit[689]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice" pid=689 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[689]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice//gpg" pid=689 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani systemd[1]: Starting Userspace Out-Of-Memory (OOM) Killer...
Jun 24 07:53:41 galelhiani systemd[1]: Starting Network Time Synchronization...
Jun 24 07:53:41 galelhiani systemd[1]: Starting Record System Boot/Shutdown in UTMP...
Jun 24 07:53:41 galelhiani systemd[1]: Finished Load AppArmor profiles.
Jun 24 07:53:41 galelhiani systemd[1]: Mounted Arbitrary Executable File Formats File System.
Jun 24 07:53:41 galelhiani systemd[1]: Finished Set Up Additional Binary Formats.
Jun 24 07:53:41 galelhiani systemd[1]: Starting Load AppArmor profiles managed internally by snapd...
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Authentication service for virtual machines hosted on VMware being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Service for virtual machines hosted on VMware being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Starting Cloud-init: Local Stage (pre-network)...
Jun 24 07:53:41 galelhiani systemd[1]: Finished Record System Boot/Shutdown in UTMP.
Jun 24 07:53:41 galelhiani snapd-apparmor[765]: main.go:146: Loading profiles [/var/lib/snapd/apparmor/profiles/snap-confine.snapd.21761 /var/lib/snapd/apparmor/profiles/snap-confine.snapd.26869 /var/lib/snapd/apparmor/profiles/snap-update-ns.firefox /var/lib/snapd/apparmor/profiles/snap-update-ns.lxd /var/lib/snapd/apparmor/profiles/snap-update-ns.mesa-2404 /var/lib/snapd/apparmor/profiles/snap.firefox.firefox /var/lib/snapd/apparmor/profiles/snap.firefox.geckodriver /var/lib/snapd/apparmor/profiles/snap.firefox.hook.configure /var/lib/snapd/apparmor/profiles/snap.firefox.hook.disconnect-plug-host-hunspell /var/lib/snapd/apparmor/profiles/snap.firefox.hook.install /var/lib/snapd/apparmor/profiles/snap.firefox.hook.post-refresh /var/lib/snapd/apparmor/profiles/snap.lxd.activate /var/lib/snapd/apparmor/profiles/snap.lxd.benchmark /var/lib/snapd/apparmor/profiles/snap.lxd.buginfo /var/lib/snapd/apparmor/profiles/snap.lxd.check-kernel /var/lib/snapd/apparmor/profiles/snap.lxd.daemon /var/lib/snapd/apparmor/profiles/snap.lxd.hook.configure /var/lib/snapd/apparmor/profiles/snap.lxd.hook.install /var/lib/snapd/apparmor/profiles/snap.lxd.hook.remove /var/lib/snapd/apparmor/profiles/snap.lxd.lxc /var/lib/snapd/apparmor/profiles/snap.lxd.lxc-to-lxd /var/lib/snapd/apparmor/profiles/snap.lxd.lxd /var/lib/snapd/apparmor/profiles/snap.lxd.migrate /var/lib/snapd/apparmor/profiles/snap.lxd.user-daemon /var/lib/snapd/apparmor/profiles/snap.mesa-2404.component-monitor /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.connect-plug-kernel-gpu-2404 /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.disconnect-plug-kernel-gpu-2404 /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.install /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.post-refresh]
Jun 24 07:53:41 galelhiani audit[792]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.lxd" pid=792 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[793]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.mesa-2404" pid=793 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[790]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/26869/usr/lib/snapd/snap-confine" pid=790 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[789]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/21761/usr/lib/snapd/snap-confine" pid=789 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[789]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/21761/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=789 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[791]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.firefox" pid=791 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[799]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.disconnect-plug-host-hunspell" pid=799 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[794]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.firefox" pid=794 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[800]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.install" pid=800 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[801]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.post-refresh" pid=801 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani systemd[1]: Started Userspace Out-Of-Memory (OOM) Killer.
Jun 24 07:53:41 galelhiani audit[797]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.geckodriver" pid=797 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[798]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.configure" pid=798 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[804]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.benchmark" pid=804 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in OpenVSwitch configuration for cleanup being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 07:53:41 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 07:53:41 galelhiani audit[805]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.buginfo" pid=805 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[806]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.check-kernel" pid=806 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 07:53:41 galelhiani systemd[1]: Started Network Time Synchronization.
Jun 24 07:53:41 galelhiani systemd[1]: Reached target System Time Set.
Jun 24 07:53:41 galelhiani audit[803]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.activate" pid=803 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[808]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.hook.configure" pid=808 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[811]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.hook.remove" pid=811 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[807]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.daemon" pid=807 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[813]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.lxc" pid=813 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[814]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.lxc-to-lxd" pid=814 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[815]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.lxd" pid=815 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[816]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.migrate" pid=816 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[818]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.component-monitor" pid=818 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[820]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.disconnect-plug-kernel-gpu-2404" pid=820 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[817]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.user-daemon" pid=817 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[821]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.install" pid=821 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[809]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.hook.install" pid=809 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[822]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.post-refresh" pid=822 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani audit[819]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.connect-plug-kernel-gpu-2404" pid=819 comm="apparmor_parser"
Jun 24 07:53:41 galelhiani systemd[1]: Finished Load AppArmor profiles managed internally by snapd.
Jun 24 07:53:41 galelhiani cloud-init[827]: Cloud-init v. 26.1-0ubuntu1~22.04.1 running 'init-local' at Wed, 24 Jun 2026 07:53:41 +0000. Up 2.92 seconds.
Jun 24 07:53:41 galelhiani systemd[1]: Finished Cloud-init: Local Stage (pre-network).
Jun 24 07:53:41 galelhiani systemd[1]: Reached target Preparation for Network.
Jun 24 07:53:41 galelhiani systemd[1]: Starting Network Configuration...
Jun 24 07:53:41 galelhiani systemd-networkd[830]: lo: Link UP
Jun 24 07:53:41 galelhiani systemd-networkd[830]: lo: Gained carrier
Jun 24 07:53:41 galelhiani systemd-networkd[830]: Enumeration completed
Jun 24 07:53:41 galelhiani systemd[1]: Started Network Configuration.
Jun 24 07:53:41 galelhiani systemd[1]: Starting Wait for Network to be Configured...
Jun 24 07:53:41 galelhiani systemd-networkd[830]: enp0s1: Link UP
Jun 24 07:53:41 galelhiani systemd[1]: Starting Network Name Resolution...
Jun 24 07:53:41 galelhiani systemd-resolved[832]: Positive Trust Anchors:
Jun 24 07:53:41 galelhiani systemd-resolved[832]: . IN DS 20326 8 2 e06d44b80b8f1d39a95c0b0d7c65d08458e880409bbc683457104237c7f8ec8d
Jun 24 07:53:41 galelhiani systemd-resolved[832]: Negative trust anchors: home.arpa 10.in-addr.arpa 16.172.in-addr.arpa 17.172.in-addr.arpa 18.172.in-addr.arpa 19.172.in-addr.arpa 20.172.in-addr.arpa 21.172.in-addr.arpa 22.172.in-addr.arpa 23.172.in-addr.arpa 24.172.in-addr.arpa 25.172.in-addr.arpa 26.172.in-addr.arpa 27.172.in-addr.arpa 28.172.in-addr.arpa 29.172.in-addr.arpa 30.172.in-addr.arpa 31.172.in-addr.arpa 168.192.in-addr.arpa d.f.ip6.arpa corp home internal intranet lan local private test
Jun 24 07:53:41 galelhiani systemd-networkd[830]: enp0s1: Gained carrier
Jun 24 07:53:41 galelhiani systemd-resolved[832]: Using system hostname 'galelhiani'.
Jun 24 07:53:41 galelhiani systemd[1]: Started Network Name Resolution.
Jun 24 07:53:41 galelhiani systemd[1]: Reached target Host and Network Name Lookups.
Jun 24 07:53:42 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 07:53:42 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 07:53:42 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 07:53:42 galelhiani systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 24 07:53:42 galelhiani systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 24 07:53:42 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 07:53:42 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 07:53:42 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 07:53:43 galelhiani systemd-networkd[830]: enp0s1: Gained IPv6LL
Jun 24 07:53:43 galelhiani systemd-timesyncd[725]: Network configuration changed, trying to establish connection.
Jun 24 07:54:10 galelhiani systemd[1]: systemd-fsckd.service: Deactivated successfully.
-- Boot ca0fe868ffba40ffae184eda347e0cc3 --
Jun 24 08:48:38 galelhiani kernel: Booting Linux on physical CPU 0x0000000000 [0x610f0000]
Jun 24 08:48:38 galelhiani kernel: Linux version 5.15.0-181-generic (buildd@bos03-arm64-052) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #191-Ubuntu SMP Fri May 22 19:27:05 UTC 2026 (Ubuntu 5.15.0-181.191-generic 5.15.199)
Jun 24 08:48:38 galelhiani kernel: efi: EFI v2.70 by EDK II
Jun 24 08:48:38 galelhiani kernel: efi: ACPI 2.0=0x26fbf0018 SMBIOS=0xfffff000 SMBIOS 3.0=0x26fc19000 MOKvar=0x26fba0000 RNG=0x26fbffd18 MEMRESERVE=0x26dfcab18 
Jun 24 08:48:38 galelhiani kernel: random: crng init done
Jun 24 08:48:38 galelhiani kernel: secureboot: Secure boot disabled
Jun 24 08:48:38 galelhiani kernel: ACPI: Early table checksum verification disabled
Jun 24 08:48:38 galelhiani kernel: ACPI: RSDP 0x000000026FBF0018 000024 (v02 APPLE )
Jun 24 08:48:38 galelhiani kernel: ACPI: XSDT 0x000000026FBFFE98 000044 (v01 APPLE  Apple Vz 00000001      01000013)
Jun 24 08:48:38 galelhiani kernel: ACPI: FACP 0x000000026FBFFA98 000114 (v06 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 08:48:38 galelhiani kernel: ACPI: DSDT 0x000000026FBFF698 0003CE (v02 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 08:48:38 galelhiani kernel: ACPI: GTDT 0x000000026FBFFC18 000068 (v03 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 08:48:38 galelhiani kernel: ACPI: APIC 0x000000026FBFE998 00024C (v05 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 08:48:38 galelhiani kernel: ACPI: MCFG 0x000000026FBFFF98 00003C (v01 APPLE  Apple Vz 00000001 AAPL 20180427)
Jun 24 08:48:38 galelhiani kernel: NUMA: Failed to initialise from firmware
Jun 24 08:48:38 galelhiani kernel: NUMA: Faking a node at [mem 0x0000000070000000-0x000000026fffffff]
Jun 24 08:48:38 galelhiani kernel: NUMA: NODE_DATA [mem 0x26ef15f80-0x26ef1afff]
Jun 24 08:48:38 galelhiani kernel: Zone ranges:
Jun 24 08:48:38 galelhiani kernel:   DMA      [mem 0x0000000070000000-0x00000000ffffffff]
Jun 24 08:48:38 galelhiani kernel:   DMA32    empty
Jun 24 08:48:38 galelhiani kernel:   Normal   [mem 0x0000000100000000-0x000000026fffffff]
Jun 24 08:48:38 galelhiani kernel:   Device   empty
Jun 24 08:48:38 galelhiani kernel: Movable zone start for each node
Jun 24 08:48:38 galelhiani kernel: Early memory node ranges
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x0000000070000000-0x00000000ffffdfff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x00000000ffffe000-0x00000000ffffffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x0000000100000000-0x000000026e56ffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026e570000-0x000000026e6fffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026e700000-0x000000026fafffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026fb00000-0x000000026fb8ffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026fb90000-0x000000026fb9ffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026fba0000-0x000000026fbdffff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026fbe0000-0x000000026fc17fff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026fc18000-0x000000026fc19fff]
Jun 24 08:48:38 galelhiani kernel:   node   0: [mem 0x000000026fc1a000-0x000000026fffffff]
Jun 24 08:48:38 galelhiani kernel: Initmem setup node 0 [mem 0x0000000070000000-0x000000026fffffff]
Jun 24 08:48:38 galelhiani kernel: cma: Reserved 32 MiB at 0x00000000fd000000
Jun 24 08:48:38 galelhiani kernel: psci: probing for conduit method from ACPI.
Jun 24 08:48:38 galelhiani kernel: psci: PSCIv1.1 detected in firmware.
Jun 24 08:48:38 galelhiani kernel: psci: Using standard PSCI v0.2 function IDs
Jun 24 08:48:38 galelhiani kernel: psci: Trusted OS migration not required
Jun 24 08:48:38 galelhiani kernel: psci: SMC Calling Convention v1.1
Jun 24 08:48:38 galelhiani kernel: ACPI: SRAT not present
Jun 24 08:48:38 galelhiani kernel: percpu: Embedded 31 pages/cpu s88792 r8192 d29992 u126976
Jun 24 08:48:38 galelhiani kernel: pcpu-alloc: s88792 r8192 d29992 u126976 alloc=31*4096
Jun 24 08:48:38 galelhiani kernel: pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 [0] 4 [0] 5 
Jun 24 08:48:38 galelhiani kernel: Detected PIPT I-cache on CPU0
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Address authentication (IMP DEF algorithm)
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: GIC system register CPU interface
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Spectre-v4
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Spectre-BHB
Jun 24 08:48:38 galelhiani kernel: alternatives: patching kernel code
Jun 24 08:48:38 galelhiani kernel: Built 1 zonelists, mobility grouping on.  Total pages: 2064384
Jun 24 08:48:38 galelhiani kernel: Policy zone: Normal
Jun 24 08:48:38 galelhiani kernel: Kernel command line: BOOT_IMAGE=/vmlinuz-5.15.0-181-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro
Jun 24 08:48:38 galelhiani kernel: Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: mem auto-init: stack:off, heap alloc:on, heap free:off
Jun 24 08:48:38 galelhiani kernel: software IO TLB: mapped [mem 0x00000000f9000000-0x00000000fd000000] (64MB)
Jun 24 08:48:38 galelhiani kernel: Memory: 7975352K/8388608K available (17536K kernel code, 4602K rwdata, 14112K rodata, 9664K init, 1193K bss, 380488K reserved, 32768K cma-reserved)
Jun 24 08:48:38 galelhiani kernel: SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=6, Nodes=1
Jun 24 08:48:38 galelhiani kernel: ftrace: allocating 54682 entries in 214 pages
Jun 24 08:48:38 galelhiani kernel: ftrace: allocated 214 pages with 5 groups
Jun 24 08:48:38 galelhiani kernel: trace event string verifier disabled
Jun 24 08:48:38 galelhiani kernel: rcu: Hierarchical RCU implementation.
Jun 24 08:48:38 galelhiani kernel: rcu:         RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=6.
Jun 24 08:48:38 galelhiani kernel:         Rude variant of Tasks RCU enabled.
Jun 24 08:48:38 galelhiani kernel:         Tracing variant of Tasks RCU enabled.
Jun 24 08:48:38 galelhiani kernel: rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
Jun 24 08:48:38 galelhiani kernel: rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=6
Jun 24 08:48:38 galelhiani kernel: NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
Jun 24 08:48:38 galelhiani kernel: GICv3: GIC: Using split EOI/Deactivate mode
Jun 24 08:48:38 galelhiani kernel: GICv3: 988 SPIs implemented
Jun 24 08:48:38 galelhiani kernel: GICv3: 0 Extended SPIs implemented
Jun 24 08:48:38 galelhiani kernel: GICv3: Distributor has Range Selector support
Jun 24 08:48:38 galelhiani kernel: Root IRQ handler: gic_handle_irq
Jun 24 08:48:38 galelhiani kernel: GICv3: 16 PPIs implemented
Jun 24 08:48:38 galelhiani kernel: GICv3: CPU0: found redistributor 0 region 0:0x0000000010010000
Jun 24 08:48:38 galelhiani kernel: GICv2m: range[mem 0x1fff0000-0x1fff0fff], SPI[128:255]
Jun 24 08:48:38 galelhiani kernel: arch_timer: cp15 timer(s) running at 24.00MHz (phys).
Jun 24 08:48:38 galelhiani kernel: clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
Jun 24 08:48:38 galelhiani kernel: sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
Jun 24 08:48:38 galelhiani kernel: Console: colour dummy device 80x25
Jun 24 08:48:38 galelhiani kernel: printk: console [tty0] enabled
Jun 24 08:48:38 galelhiani kernel: ACPI: Core revision 20210730
Jun 24 08:48:38 galelhiani kernel: Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=96000)
Jun 24 08:48:38 galelhiani kernel: pid_max: default: 32768 minimum: 301
Jun 24 08:48:38 galelhiani kernel: LSM: Security Framework initializing
Jun 24 08:48:38 galelhiani kernel: landlock: Up and running.
Jun 24 08:48:38 galelhiani kernel: Yama: becoming mindful.
Jun 24 08:48:38 galelhiani kernel: AppArmor: AppArmor initialized
Jun 24 08:48:38 galelhiani kernel: Mount-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: ACPI PPTT: No PPTT table found, CPU and cache topology may be inaccurate
Jun 24 08:48:38 galelhiani kernel: rcu: Hierarchical SRCU implementation.
Jun 24 08:48:38 galelhiani kernel: Remapping and enabling EFI services.
Jun 24 08:48:38 galelhiani kernel: smp: Bringing up secondary CPUs ...
Jun 24 08:48:38 galelhiani kernel: Detected PIPT I-cache on CPU1
Jun 24 08:48:38 galelhiani kernel: GICv3: CPU1: found redistributor 1 region 0:0x0000000010030000
Jun 24 08:48:38 galelhiani kernel: CPU1: Booted secondary processor 0x0000000001 [0x610f0000]
Jun 24 08:48:38 galelhiani kernel: Detected PIPT I-cache on CPU2
Jun 24 08:48:38 galelhiani kernel: GICv3: CPU2: found redistributor 2 region 0:0x0000000010050000
Jun 24 08:48:38 galelhiani kernel: CPU2: Booted secondary processor 0x0000000002 [0x610f0000]
Jun 24 08:48:38 galelhiani kernel: Detected PIPT I-cache on CPU3
Jun 24 08:48:38 galelhiani kernel: GICv3: CPU3: found redistributor 3 region 0:0x0000000010070000
Jun 24 08:48:38 galelhiani kernel: CPU3: Booted secondary processor 0x0000000003 [0x610f0000]
Jun 24 08:48:38 galelhiani kernel: Detected PIPT I-cache on CPU4
Jun 24 08:48:38 galelhiani kernel: GICv3: CPU4: found redistributor 4 region 0:0x0000000010090000
Jun 24 08:48:38 galelhiani kernel: CPU4: Booted secondary processor 0x0000000004 [0x610f0000]
Jun 24 08:48:38 galelhiani kernel: Detected PIPT I-cache on CPU5
Jun 24 08:48:38 galelhiani kernel: GICv3: CPU5: found redistributor 5 region 0:0x00000000100b0000
Jun 24 08:48:38 galelhiani kernel: CPU5: Booted secondary processor 0x0000000005 [0x610f0000]
Jun 24 08:48:38 galelhiani kernel: smp: Brought up 1 node, 6 CPUs
Jun 24 08:48:38 galelhiani kernel: SMP: Total of 6 processors activated.
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Branch Target Identification
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: ARMv8.4 Translation Table Level
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Data cache clean to the PoU not required for I/D coherence
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Common not Private translations
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: CRC32 instructions
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Data cache clean to Point of Deep Persistence
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Data cache clean to Point of Persistence
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: E0PD
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Enhanced Privileged Access Never
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Generic authentication (IMP DEF algorithm)
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: RCpc load-acquire (LDAPR)
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: LSE atomic instructions
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Privileged Access Never
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: RAS Extension Support
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: Speculation barrier (SB)
Jun 24 08:48:38 galelhiani kernel: CPU features: detected: TLB range maintenance instructions
Jun 24 08:48:38 galelhiani kernel: CPU: All CPU(s) started at EL2
Jun 24 08:48:38 galelhiani kernel: devtmpfs: initialized
Jun 24 08:48:38 galelhiani kernel: setend instruction emulation is not supported on this system
Jun 24 08:48:38 galelhiani kernel: KASLR enabled
Jun 24 08:48:38 galelhiani kernel: clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
Jun 24 08:48:38 galelhiani kernel: futex hash table entries: 2048 (order: 5, 131072 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: pinctrl core: initialized pinctrl subsystem
Jun 24 08:48:38 galelhiani kernel: SMBIOS 3.3.0 present.
Jun 24 08:48:38 galelhiani kernel: DMI: Apple Inc. Apple Virtualization Generic Platform, BIOS 2103.100.6.0.0 04/18/2026
Jun 24 08:48:38 galelhiani kernel: NET: Registered PF_NETLINK/PF_ROUTE protocol family
Jun 24 08:48:38 galelhiani kernel: DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations
Jun 24 08:48:38 galelhiani kernel: DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
Jun 24 08:48:38 galelhiani kernel: DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
Jun 24 08:48:38 galelhiani kernel: audit: initializing netlink subsys (disabled)
Jun 24 08:48:38 galelhiani kernel: audit: type=2000 audit(0.020:1): state=initialized audit_enabled=0 res=1
Jun 24 08:48:38 galelhiani kernel: thermal_sys: Registered thermal governor 'fair_share'
Jun 24 08:48:38 galelhiani kernel: thermal_sys: Registered thermal governor 'bang_bang'
Jun 24 08:48:38 galelhiani kernel: thermal_sys: Registered thermal governor 'step_wise'
Jun 24 08:48:38 galelhiani kernel: thermal_sys: Registered thermal governor 'user_space'
Jun 24 08:48:38 galelhiani kernel: thermal_sys: Registered thermal governor 'power_allocator'
Jun 24 08:48:38 galelhiani kernel: cpuidle: using governor ladder
Jun 24 08:48:38 galelhiani kernel: cpuidle: using governor menu
Jun 24 08:48:38 galelhiani kernel: hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
Jun 24 08:48:38 galelhiani kernel: ASID allocator initialised with 65536 entries
Jun 24 08:48:38 galelhiani kernel: ACPI: bus type PCI registered
Jun 24 08:48:38 galelhiani kernel: acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
Jun 24 08:48:38 galelhiani kernel: Serial: AMBA PL011 UART driver
Jun 24 08:48:38 galelhiani kernel: HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
Jun 24 08:48:38 galelhiani kernel: HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
Jun 24 08:48:38 galelhiani kernel: HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
Jun 24 08:48:38 galelhiani kernel: HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
Jun 24 08:48:38 galelhiani kernel: fbcon: Taking over console
Jun 24 08:48:38 galelhiani kernel: ACPI: Added _OSI(Module Device)
Jun 24 08:48:38 galelhiani kernel: ACPI: Added _OSI(Processor Device)
Jun 24 08:48:38 galelhiani kernel: ACPI: Added _OSI(Processor Aggregator Device)
Jun 24 08:48:38 galelhiani kernel: ACPI: Added _OSI(Linux-Dell-Video)
Jun 24 08:48:38 galelhiani kernel: ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
Jun 24 08:48:38 galelhiani kernel: ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
Jun 24 08:48:38 galelhiani kernel: ACPI: 1 ACPI AML tables successfully acquired and loaded
Jun 24 08:48:38 galelhiani kernel: ACPI: Interpreter enabled
Jun 24 08:48:38 galelhiani kernel: ACPI: Using GIC for interrupt routing
Jun 24 08:48:38 galelhiani kernel: ACPI: MCFG table detected, 1 entries
Jun 24 08:48:38 galelhiani kernel: ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
Jun 24 08:48:38 galelhiani kernel: acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI EDR HPX-Type3]
Jun 24 08:48:38 galelhiani kernel: acpi PNP0A08:00: _OSC: platform retains control of PCIe features (AE_NOT_FOUND)
Jun 24 08:48:38 galelhiani kernel: acpi PNP0A08:00: ECAM area [mem 0x40000000-0x4fffffff] reserved by PNP0C02:00
Jun 24 08:48:38 galelhiani kernel: acpi PNP0A08:00: ECAM at [mem 0x40000000-0x4fffffff] for [bus 00-ff]
Jun 24 08:48:38 galelhiani kernel: ACPI: Remapped I/O 0x000000006fff0000 to [io  0x0000-0xffff window]
Jun 24 08:48:38 galelhiani kernel: PCI host bridge to bus 0000:00
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: root bus resource [mem 0x50000000-0x6ffdffff window]
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: root bus resource [mem 0x280000000-0x67fffffff window]
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: root bus resource [io  0x0000-0xffff window]
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: root bus resource [bus 00-ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:00.0: [106b:1a05] type 00 class 0x060000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:01.0: [1af4:1041] type 00 class 0x020000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:01.0: reg 0x10: [mem 0x280080000-0x28008ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:01.0: reg 0x18: [mem 0x5000d000-0x5000d03f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:05.0: [1af4:1042] type 00 class 0x018000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:05.0: reg 0x10: [mem 0x280070000-0x28007ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:05.0: reg 0x18: [mem 0x5000c000-0x5000c03f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:06.0: [1af4:105a] type 00 class 0x018000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:06.0: reg 0x10: [mem 0x280060000-0x28006ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:06.0: reg 0x18: [mem 0x5000b000-0x5000b03f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:07.0: [1af4:105a] type 00 class 0x018000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:07.0: reg 0x10: [mem 0x280050000-0x28005ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:07.0: reg 0x18: [mem 0x5000a000-0x5000a03f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:08.0: [1af4:1050] type 00 class 0x038000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:08.0: reg 0x10: [mem 0x280040000-0x28004ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:08.0: reg 0x18: [mem 0x50009000-0x5000903f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:09.0: [1af4:1059] type 00 class 0x040100
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:09.0: reg 0x10: [mem 0x280030000-0x28003ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:09.0: reg 0x18: [mem 0x50006000-0x5000607f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0a.0: [1af4:1059] type 00 class 0x040100
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0a.0: reg 0x10: [mem 0x280020000-0x28002ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0a.0: reg 0x18: [mem 0x50005000-0x5000507f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0b.0: [1af4:1044] type 00 class 0x100000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0b.0: reg 0x10: [mem 0x280090000-0x280097fff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0b.0: reg 0x18: [mem 0x50008000-0x5000803f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0c.0: [1af4:1045] type 00 class 0x058000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0c.0: reg 0x10: [mem 0x280010000-0x28001ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0c.0: reg 0x18: [mem 0x50007000-0x5000703f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0d.0: [1af4:1043] type 00 class 0x078000
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0d.0: reg 0x10: [mem 0x280000000-0x28000ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0d.0: reg 0x18: [mem 0x50004000-0x5000407f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0e.0: [106b:1a06] type 00 class 0x0c0330
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0e.0: reg 0x10: [mem 0x50003000-0x50003fff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0e.0: reg 0x14: [mem 0x50002000-0x500023ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0f.0: [106b:1a06] type 00 class 0x0c0330
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0f.0: reg 0x10: [mem 0x50001000-0x50001fff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0f.0: reg 0x14: [mem 0x50000000-0x500003ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:01.0: BAR 0: assigned [mem 0x280000000-0x28000ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:05.0: BAR 0: assigned [mem 0x280010000-0x28001ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:06.0: BAR 0: assigned [mem 0x280020000-0x28002ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:07.0: BAR 0: assigned [mem 0x280030000-0x28003ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:08.0: BAR 0: assigned [mem 0x280040000-0x28004ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:09.0: BAR 0: assigned [mem 0x280050000-0x28005ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0a.0: BAR 0: assigned [mem 0x280060000-0x28006ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0c.0: BAR 0: assigned [mem 0x280070000-0x28007ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0d.0: BAR 0: assigned [mem 0x280080000-0x28008ffff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0b.0: BAR 0: assigned [mem 0x280090000-0x280097fff 64bit]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0e.0: BAR 0: assigned [mem 0x50000000-0x50000fff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0f.0: BAR 0: assigned [mem 0x50001000-0x50001fff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0e.0: BAR 1: assigned [mem 0x50002000-0x500023ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0f.0: BAR 1: assigned [mem 0x50002400-0x500027ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:09.0: BAR 2: assigned [mem 0x50002800-0x5000287f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0a.0: BAR 2: assigned [mem 0x50002880-0x500028ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0d.0: BAR 2: assigned [mem 0x50002900-0x5000297f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:01.0: BAR 2: assigned [mem 0x50002980-0x500029bf]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:05.0: BAR 2: assigned [mem 0x500029c0-0x500029ff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:06.0: BAR 2: assigned [mem 0x50002a00-0x50002a3f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:07.0: BAR 2: assigned [mem 0x50002a40-0x50002a7f]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:08.0: BAR 2: assigned [mem 0x50002a80-0x50002abf]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0b.0: BAR 2: assigned [mem 0x50002ac0-0x50002aff]
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0c.0: BAR 2: assigned [mem 0x50002b00-0x50002b3f]
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: resource 4 [mem 0x50000000-0x6ffdffff window]
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: resource 5 [mem 0x280000000-0x67fffffff window]
Jun 24 08:48:38 galelhiani kernel: pci_bus 0000:00: resource 6 [io  0x0000-0xffff window]
Jun 24 08:48:38 galelhiani kernel: iommu: Default domain type: Translated 
Jun 24 08:48:38 galelhiani kernel: iommu: DMA domain TLB invalidation policy: strict mode 
Jun 24 08:48:38 galelhiani kernel: SCSI subsystem initialized
Jun 24 08:48:38 galelhiani kernel: libata version 3.00 loaded.
Jun 24 08:48:38 galelhiani kernel: vgaarb: loaded
Jun 24 08:48:38 galelhiani kernel: ACPI: bus type USB registered
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new interface driver usbfs
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new interface driver hub
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new device driver usb
Jun 24 08:48:38 galelhiani kernel: pps_core: LinuxPPS API ver. 1 registered
Jun 24 08:48:38 galelhiani kernel: pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
Jun 24 08:48:38 galelhiani kernel: PTP clock support registered
Jun 24 08:48:38 galelhiani kernel: EDAC MC: Ver: 3.0.0
Jun 24 08:48:38 galelhiani kernel: Registered efivars operations
Jun 24 08:48:38 galelhiani kernel: NetLabel: Initializing
Jun 24 08:48:38 galelhiani kernel: NetLabel:  domain hash size = 128
Jun 24 08:48:38 galelhiani kernel: NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
Jun 24 08:48:38 galelhiani kernel: NetLabel:  unlabeled traffic allowed by default
Jun 24 08:48:38 galelhiani kernel: clocksource: Switched to clocksource arch_sys_counter
Jun 24 08:48:38 galelhiani kernel: VFS: Disk quotas dquot_6.6.0
Jun 24 08:48:38 galelhiani kernel: VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
Jun 24 08:48:38 galelhiani kernel: AppArmor: AppArmor Filesystem Enabled
Jun 24 08:48:38 galelhiani kernel: pnp: PnP ACPI init
Jun 24 08:48:38 galelhiani kernel: system 00:00: [mem 0x40000000-0x4fffffff] could not be reserved
Jun 24 08:48:38 galelhiani kernel: pnp: PnP ACPI: found 1 devices
Jun 24 08:48:38 galelhiani kernel: NET: Registered PF_INET protocol family
Jun 24 08:48:38 galelhiani kernel: IP idents hash table entries: 131072 (order: 8, 1048576 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: TCP established hash table entries: 65536 (order: 7, 524288 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: TCP: Hash tables configured (established 65536 bind 65536)
Jun 24 08:48:38 galelhiani kernel: MPTCP token hash table entries: 8192 (order: 6, 196608 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: UDP hash table entries: 4096 (order: 5, 131072 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes, linear)
Jun 24 08:48:38 galelhiani kernel: NET: Registered PF_UNIX/PF_LOCAL protocol family
Jun 24 08:48:38 galelhiani kernel: NET: Registered PF_XDP protocol family
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0e.0: enabling device (0010 -> 0012)
Jun 24 08:48:38 galelhiani kernel: pci 0000:00:0f.0: enabling device (0010 -> 0012)
Jun 24 08:48:38 galelhiani kernel: PCI: CLS 0 bytes, default 64
Jun 24 08:48:38 galelhiani kernel: Trying to unpack rootfs image as initramfs...
Jun 24 08:48:38 galelhiani kernel: kvm [1]: IPA Size Limit: 40 bits
Jun 24 08:48:38 galelhiani kernel: kvm [1]: GICv3: no GICV resource entry
Jun 24 08:48:38 galelhiani kernel: kvm [1]: disabling GICv2 emulation
Jun 24 08:48:38 galelhiani kernel: kvm [1]: GIC system register CPU interface enabled
Jun 24 08:48:38 galelhiani kernel: kvm [1]: vgic interrupt IRQ9
Jun 24 08:48:38 galelhiani kernel: kvm [1]: Hyp mode initialized successfully
Jun 24 08:48:38 galelhiani kernel: Initialise system trusted keyrings
Jun 24 08:48:38 galelhiani kernel: Key type blacklist registered
Jun 24 08:48:38 galelhiani kernel: workingset: timestamp_bits=40 max_order=21 bucket_order=0
Jun 24 08:48:38 galelhiani kernel: zbud: loaded
Jun 24 08:48:38 galelhiani kernel: squashfs: version 4.0 (2009/01/31) Phillip Lougher
Jun 24 08:48:38 galelhiani kernel: fuse: init (API version 7.34)
Jun 24 08:48:38 galelhiani kernel: integrity: Platform Keyring initialized
Jun 24 08:48:38 galelhiani kernel: Key type asymmetric registered
Jun 24 08:48:38 galelhiani kernel: Asymmetric key parser 'x509' registered
Jun 24 08:48:38 galelhiani kernel: Block layer SCSI generic (bsg) driver version 0.4 loaded (major 242)
Jun 24 08:48:38 galelhiani kernel: io scheduler mq-deadline registered
Jun 24 08:48:38 galelhiani kernel: pl061_gpio ARMH0061:00: PL061 GPIO chip registered
Jun 24 08:48:38 galelhiani kernel: shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
Jun 24 08:48:38 galelhiani kernel: input: Power Button as /devices/LNXSYSTM:00/PNP0C0C:00/input/input0
Jun 24 08:48:38 galelhiani kernel: ACPI: button: Power Button [PWRB]
Jun 24 08:48:38 galelhiani kernel: Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
Jun 24 08:48:38 galelhiani kernel: SuperH (H)SCI(F) driver initialized
Jun 24 08:48:38 galelhiani kernel: msm_serial: driver initialized
Jun 24 08:48:38 galelhiani kernel: cacheinfo: Unable to detect cache hierarchy for CPU 0
Jun 24 08:48:38 galelhiani kernel: loop: module loaded
Jun 24 08:48:38 galelhiani kernel: SPI driver altr_a10sr has no spi_device_id for altr,a10sr
Jun 24 08:48:38 galelhiani kernel: tun: Universal TUN/TAP device driver, 1.6
Jun 24 08:48:38 galelhiani kernel: PPP generic driver version 2.4.2
Jun 24 08:48:38 galelhiani kernel: ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
Jun 24 08:48:38 galelhiani kernel: ehci-pci: EHCI PCI platform driver
Jun 24 08:48:38 galelhiani kernel: ehci-orion: EHCI orion driver
Jun 24 08:48:38 galelhiani kernel: ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
Jun 24 08:48:38 galelhiani kernel: ohci-pci: OHCI PCI platform driver
Jun 24 08:48:38 galelhiani kernel: uhci_hcd: USB Universal Host Controller Interface driver
Jun 24 08:48:38 galelhiani kernel: mousedev: PS/2 mouse device common for all mice
Jun 24 08:48:38 galelhiani kernel: rtc-efi rtc-efi.0: registered as rtc0
Jun 24 08:48:38 galelhiani kernel: rtc-efi rtc-efi.0: setting system clock to 2026-06-24T08:48:36 UTC (1782290916)
Jun 24 08:48:38 galelhiani kernel: i2c_dev: i2c /dev entries driver
Jun 24 08:48:38 galelhiani kernel: device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
Jun 24 08:48:38 galelhiani kernel: device-mapper: uevent: version 1.0.3
Jun 24 08:48:38 galelhiani kernel: device-mapper: ioctl: 4.45.0-ioctl (2021-03-22) initialised: dm-devel@redhat.com
Jun 24 08:48:38 galelhiani kernel: ledtrig-cpu: registered to indicate activity on CPUs
Jun 24 08:48:38 galelhiani kernel: drop_monitor: Initializing network drop monitor service
Jun 24 08:48:38 galelhiani kernel: NET: Registered PF_INET6 protocol family
Jun 24 08:48:38 galelhiani kernel: Freeing initrd memory: 103836K
Jun 24 08:48:38 galelhiani kernel: Segment Routing with IPv6
Jun 24 08:48:38 galelhiani kernel: In-situ OAM (IOAM) with IPv6
Jun 24 08:48:38 galelhiani kernel: NET: Registered PF_PACKET protocol family
Jun 24 08:48:38 galelhiani kernel: Key type dns_resolver registered
Jun 24 08:48:38 galelhiani kernel: registered taskstats version 1
Jun 24 08:48:38 galelhiani kernel: Loading compiled-in X.509 certificates
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Build time autogenerated kernel key: a112623dda86549bada95b36cd50fc4d89454411'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Live Patch Signing 2025 Kmod: d541cef61dc7e793b7eb7e899970a2eef0b5dc8c'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing 2025 Kmod: 4627603d2357a2a3f81006370894c221175893e9'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
Jun 24 08:48:38 galelhiani kernel: blacklist: Loading compiled-in revocation X.509 certificates
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing: 61482aa2830d0ab2ad5af10b7250da9033ddcef0'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2017): 242ade75ac4a15e50d50c84b0d45ff3eae707a03'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (ESM 2018): 365188c1d374d6b07c3c8f240f8ef722433d6a8b'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2019): c0746fd6c5da3ae827864651ad66ae47fe24b3e8'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v1): a8d54bbb3825cfb94fa13c9f8a594a195c107b8d'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v2): 4cf046892d6fd3c9a5b03f98d845f90851dc6a8c'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af'
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Canonical Ltd. Secure Boot Signing (Ubuntu Core 2019): c1d57b8f6b743f23ee41f4f7ee292f06eecadfb9'
Jun 24 08:48:38 galelhiani kernel: zswap: loaded using pool lzo/zbud
Jun 24 08:48:38 galelhiani kernel: Key type .fscrypt registered
Jun 24 08:48:38 galelhiani kernel: Key type fscrypt-provisioning registered
Jun 24 08:48:38 galelhiani kernel: cryptd: max_cpu_qlen set to 1000
Jun 24 08:48:38 galelhiani kernel: Key type encrypted registered
Jun 24 08:48:38 galelhiani kernel: AppArmor: AppArmor sha1 policy hashing enabled
Jun 24 08:48:38 galelhiani kernel: integrity: Loading X.509 certificate: UEFI:MokListRT (MOKvar table)
Jun 24 08:48:38 galelhiani kernel: integrity: Loaded X.509 cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63'
Jun 24 08:48:38 galelhiani kernel: ima: No TPM chip found, activating TPM-bypass!
Jun 24 08:48:38 galelhiani kernel: Loading compiled-in module X.509 certificates
Jun 24 08:48:38 galelhiani kernel: Loaded X.509 cert 'Build time autogenerated kernel key: a112623dda86549bada95b36cd50fc4d89454411'
Jun 24 08:48:38 galelhiani kernel: ima: Allocated hash algorithm: sha1
Jun 24 08:48:38 galelhiani kernel: ima: No architecture policies found
Jun 24 08:48:38 galelhiani kernel: evm: Initialising EVM extended attributes:
Jun 24 08:48:38 galelhiani kernel: evm: security.selinux
Jun 24 08:48:38 galelhiani kernel: evm: security.SMACK64
Jun 24 08:48:38 galelhiani kernel: evm: security.SMACK64EXEC
Jun 24 08:48:38 galelhiani kernel: evm: security.SMACK64TRANSMUTE
Jun 24 08:48:38 galelhiani kernel: evm: security.SMACK64MMAP
Jun 24 08:48:38 galelhiani kernel: evm: security.apparmor
Jun 24 08:48:38 galelhiani kernel: evm: security.ima
Jun 24 08:48:38 galelhiani kernel: evm: security.capability
Jun 24 08:48:38 galelhiani kernel: evm: HMAC attrs: 0x1
Jun 24 08:48:38 galelhiani kernel: clk: Disabling unused clocks
Jun 24 08:48:38 galelhiani kernel: Freeing unused kernel memory: 9664K
Jun 24 08:48:38 galelhiani kernel: Checked W+X mappings: passed, no W+X pages found
Jun 24 08:48:38 galelhiani kernel: Run /init as init process
Jun 24 08:48:38 galelhiani kernel:   with arguments:
Jun 24 08:48:38 galelhiani kernel:     /init
Jun 24 08:48:38 galelhiani kernel:   with environment:
Jun 24 08:48:38 galelhiani kernel:     HOME=/
Jun 24 08:48:38 galelhiani kernel:     TERM=linux
Jun 24 08:48:38 galelhiani kernel: virtio_blk virtio1: [vda] 209715200 512-byte logical blocks (107 GB/100 GiB)
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0e.0: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0e.0: new USB bus registered, assigned bus number 1
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0e.0: hcc params 0x02600801 hci version 0x110 quirks 0x0000000000000010
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0e.0: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0e.0: new USB bus registered, assigned bus number 2
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0e.0: Host supports USB 3.1 Enhanced SuperSpeed
Jun 24 08:48:38 galelhiani kernel: usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
Jun 24 08:48:38 galelhiani kernel: usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 08:48:38 galelhiani kernel: usb usb1: Product: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: usb usb1: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 08:48:38 galelhiani kernel: usb usb1: SerialNumber: 0000:00:0e.0
Jun 24 08:48:38 galelhiani kernel: hub 1-0:1.0: USB hub found
Jun 24 08:48:38 galelhiani kernel: hub 1-0:1.0: 8 ports detected
Jun 24 08:48:38 galelhiani kernel: usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
Jun 24 08:48:38 galelhiani kernel: usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
Jun 24 08:48:38 galelhiani kernel: usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 08:48:38 galelhiani kernel: usb usb2: Product: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: usb usb2: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 08:48:38 galelhiani kernel: usb usb2: SerialNumber: 0000:00:0e.0
Jun 24 08:48:38 galelhiani kernel: hub 2-0:1.0: USB hub found
Jun 24 08:48:38 galelhiani kernel: hub 2-0:1.0: 8 ports detected
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0f.0: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0f.0: new USB bus registered, assigned bus number 3
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0f.0: hcc params 0x02600801 hci version 0x110 quirks 0x0000000000000010
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0f.0: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0f.0: new USB bus registered, assigned bus number 4
Jun 24 08:48:38 galelhiani kernel: xhci_hcd 0000:00:0f.0: Host supports USB 3.1 Enhanced SuperSpeed
Jun 24 08:48:38 galelhiani kernel: usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
Jun 24 08:48:38 galelhiani kernel: usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 08:48:38 galelhiani kernel: usb usb3: Product: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: usb usb3: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 08:48:38 galelhiani kernel: usb usb3: SerialNumber: 0000:00:0f.0
Jun 24 08:48:38 galelhiani kernel: hub 3-0:1.0: USB hub found
Jun 24 08:48:38 galelhiani kernel: hub 3-0:1.0: 8 ports detected
Jun 24 08:48:38 galelhiani kernel: usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
Jun 24 08:48:38 galelhiani kernel: usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.15
Jun 24 08:48:38 galelhiani kernel: usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Jun 24 08:48:38 galelhiani kernel: usb usb4: Product: xHCI Host Controller
Jun 24 08:48:38 galelhiani kernel: usb usb4: Manufacturer: Linux 5.15.0-181-generic xhci-hcd
Jun 24 08:48:38 galelhiani kernel: usb usb4: SerialNumber: 0000:00:0f.0
Jun 24 08:48:38 galelhiani kernel: hub 4-0:1.0: USB hub found
Jun 24 08:48:38 galelhiani kernel: hub 4-0:1.0: 8 ports detected
Jun 24 08:48:38 galelhiani kernel:  vda: vda1 vda2 vda3
Jun 24 08:48:38 galelhiani kernel: [drm] pci: virtio-gpu-pci detected at 0000:00:08.0
Jun 24 08:48:38 galelhiani kernel: [drm] features: -virgl -edid -resource_blob -host_visible
Jun 24 08:48:38 galelhiani kernel: [drm] number of scanouts: 1
Jun 24 08:48:38 galelhiani kernel: [drm] number of cap sets: 0
Jun 24 08:48:38 galelhiani kernel: [drm] Initialized virtio_gpu 0.1.0 0 for virtio4 on minor 0
Jun 24 08:48:38 galelhiani kernel: virtio_gpu virtio4: [drm] drm_plane_enable_fb_damage_clips() not called
Jun 24 08:48:38 galelhiani kernel: Console: switching to colour frame buffer device 166x52
Jun 24 08:48:38 galelhiani kernel: virtio_gpu virtio4: [drm] fb0: virtio_gpudrmfb frame buffer device
Jun 24 08:48:38 galelhiani kernel: virtio_net virtio0 enp0s1: renamed from eth0
Jun 24 08:48:38 galelhiani kernel: usb 1-1: new full-speed USB device number 2 using xhci_hcd
Jun 24 08:48:38 galelhiani kernel: usb 4-1: new SuperSpeed USB device number 2 using xhci_hcd
Jun 24 08:48:38 galelhiani kernel: usb 4-1: New USB device found, idVendor=05ac, idProduct=1503, bcdDevice= 0.00
Jun 24 08:48:38 galelhiani kernel: usb 4-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Jun 24 08:48:38 galelhiani kernel: usb 4-1: Product: Virtual USB Mass Storage Device
Jun 24 08:48:38 galelhiani kernel: usb 4-1: Manufacturer: Apple Inc.
Jun 24 08:48:38 galelhiani kernel: usb-storage 4-1:1.0: USB Mass Storage device detected
Jun 24 08:48:38 galelhiani kernel: scsi host0: usb-storage 4-1:1.0
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new interface driver usb-storage
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new interface driver uas
Jun 24 08:48:38 galelhiani kernel: raid6: neonx8   gen() 44252 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: neonx8   xor() 44131 MB/s
Jun 24 08:48:38 galelhiani kernel: usb 1-1: New USB device found, idVendor=05ac, idProduct=8105, bcdDevice= 0.00
Jun 24 08:48:38 galelhiani kernel: usb 1-1: New USB device strings: Mfr=2, Product=3, SerialNumber=0
Jun 24 08:48:38 galelhiani kernel: usb 1-1: Product: Virtual USB Keyboard
Jun 24 08:48:38 galelhiani kernel: usb 1-1: Manufacturer: Apple Inc.
Jun 24 08:48:38 galelhiani kernel: raid6: neonx4   gen() 49798 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: neonx4   xor() 44956 MB/s
Jun 24 08:48:38 galelhiani kernel: usb 1-2: new full-speed USB device number 3 using xhci_hcd
Jun 24 08:48:38 galelhiani kernel: raid6: neonx2   gen() 52746 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: neonx2   xor() 44529 MB/s
Jun 24 08:48:38 galelhiani kernel: usb 1-2: New USB device found, idVendor=05ac, idProduct=8106, bcdDevice= 0.00
Jun 24 08:48:38 galelhiani kernel: usb 1-2: New USB device strings: Mfr=2, Product=3, SerialNumber=0
Jun 24 08:48:38 galelhiani kernel: usb 1-2: Product: Virtual USB Digitizer
Jun 24 08:48:38 galelhiani kernel: usb 1-2: Manufacturer: Apple Inc.
Jun 24 08:48:38 galelhiani kernel: hid: raw HID events driver (C) Jiri Kosina
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new interface driver usbhid
Jun 24 08:48:38 galelhiani kernel: usbhid: USB HID core driver
Jun 24 08:48:38 galelhiani kernel: input: Apple Inc. Virtual USB Keyboard as /devices/pci0000:00/0000:00:0e.0/usb1/1-1/1-1:1.0/0003:05AC:8105.0001/input/input1
Jun 24 08:48:38 galelhiani kernel: raid6: neonx1   gen() 52672 MB/s
Jun 24 08:48:38 galelhiani kernel: hid-generic 0003:05AC:8105.0001: input,hidraw0: USB HID v1.10 Keyboard [Apple Inc. Virtual USB Keyboard] on usb-0000:00:0e.0-1/input0
Jun 24 08:48:38 galelhiani kernel: input: Apple Inc. Virtual USB Digitizer as /devices/pci0000:00/0000:00:0e.0/usb1/1-2/1-2:1.0/0003:05AC:8106.0002/input/input2
Jun 24 08:48:38 galelhiani kernel: hid-generic 0003:05AC:8106.0002: input,hidraw1: USB HID v1.10 Mouse [Apple Inc. Virtual USB Digitizer] on usb-0000:00:0e.0-2/input0
Jun 24 08:48:38 galelhiani kernel: raid6: neonx1   xor() 39000 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x8  gen() 25244 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x8  xor() 13997 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x4  gen() 23551 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x4  xor() 12826 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x2  gen() 20556 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x2  xor() 10883 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: int64x1  gen() 17965 MB/s
Jun 24 08:48:38 galelhiani kernel: scsi 0:0:0:0: Direct-Access     Apple    Virtual Disk     1    PQ: 0 ANSI: 6
Jun 24 08:48:38 galelhiani kernel: sd 0:0:0:0: Attached scsi generic sg0 type 0
Jun 24 08:48:38 galelhiani kernel: sd 0:0:0:0: [sda] 4027128 512-byte logical blocks: (2.06 GB/1.92 GiB)
Jun 24 08:48:38 galelhiani kernel: sd 0:0:0:0: [sda] Write Protect is on
Jun 24 08:48:38 galelhiani kernel: sd 0:0:0:0: [sda] Mode Sense: 21 00 80 00
Jun 24 08:48:38 galelhiani kernel: sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
Jun 24 08:48:38 galelhiani kernel:  sda: sda1 sda2
Jun 24 08:48:38 galelhiani kernel: sd 0:0:0:0: [sda] Attached SCSI disk
Jun 24 08:48:38 galelhiani kernel: raid6: int64x1  xor()  9213 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: using algorithm neonx2 gen() 52746 MB/s
Jun 24 08:48:38 galelhiani kernel: raid6: .... xor() 44529 MB/s, rmw enabled
Jun 24 08:48:38 galelhiani kernel: raid6: using neon recovery algorithm
Jun 24 08:48:38 galelhiani kernel: xor: measuring software checksum speed
Jun 24 08:48:38 galelhiani kernel:    8regs           : 51465 MB/sec
Jun 24 08:48:38 galelhiani kernel:    32regs          : 74848 MB/sec
Jun 24 08:48:38 galelhiani kernel:    arm64_neon      : 80760 MB/sec
Jun 24 08:48:38 galelhiani kernel: xor: using function: arm64_neon (80760 MB/sec)
Jun 24 08:48:38 galelhiani kernel: async_tx: api initialized (async)
Jun 24 08:48:38 galelhiani kernel: Btrfs loaded, crc32c=crc32c-generic, zoned=yes, fsverity=yes
Jun 24 08:48:38 galelhiani kernel: EXT4-fs (dm-0): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
Jun 24 08:48:38 galelhiani systemd[1]: Inserted module 'autofs4'
Jun 24 08:48:38 galelhiani systemd[1]: systemd 249.11-0ubuntu3.21 running in system mode (+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified)
Jun 24 08:48:38 galelhiani systemd[1]: Detected architecture arm64.
Jun 24 08:48:38 galelhiani systemd[1]: Hostname set to <galelhiani>.
Jun 24 08:48:38 galelhiani systemd[1]: Configuration file /run/systemd/system/netplan-ovs-cleanup.service is marked world-inaccessible. This has no effect as configuration data is accessible via APIs without restrictions. Proceeding anyway.
Jun 24 08:48:38 galelhiani systemd[1]: /lib/systemd/system/snapd.service:23: Unknown key name 'RestartMode' in section 'Service', ignoring.
Jun 24 08:48:38 galelhiani systemd[1]: Queued start job for default target Graphical Interface.
Jun 24 08:48:38 galelhiani systemd[1]: Created slice Slice /system/modprobe.
Jun 24 08:48:38 galelhiani systemd[1]: Created slice Slice /system/systemd-fsck.
Jun 24 08:48:38 galelhiani systemd[1]: Created slice User and Session Slice.
Jun 24 08:48:38 galelhiani systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Jun 24 08:48:38 galelhiani systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Slice Units.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Mounting snaps.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Local Verity Protected Volumes.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Device-mapper event daemon FIFOs.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on LVM2 poll daemon socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on multipathd control socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Syslog Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on fsck to fsckd communication Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on initctl Compatibility Named Pipe.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Journal Audit Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Journal Socket (/dev/log).
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Journal Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Network Service Netlink Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on udev Control Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Listening on udev Kernel Socket.
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Huge Pages File System...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting POSIX Message Queue File System...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Kernel Debug File System...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Kernel Trace File System...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Journal Service...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Set the console keyboard layout...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Create List of Static Device Nodes...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling...
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in LXD - agent being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load Kernel Module configfs...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load Kernel Module drm...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load Kernel Module fuse...
Jun 24 08:48:38 galelhiani systemd-journald[474]: Journal started
Jun 24 08:48:38 galelhiani systemd-journald[474]: Runtime Journal (/run/log/journal/1955aac654704d37a292a15c85e64c9d) is 8.0M, max 79.3M, 71.3M free.
Jun 24 08:48:38 galelhiani lvm[481]:   1 logical volume(s) in volume group "ubuntu-vg" monitored
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in OpenVSwitch configuration for cleanup being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
Jun 24 08:48:38 galelhiani kernel: pstore: Using crash dump compression: deflate
Jun 24 08:48:38 galelhiani kernel: pstore: Registered efi as persistent store backend
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load Kernel Modules...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Remount Root and Kernel File Systems...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Coldplug All udev Devices...
Jun 24 08:48:38 galelhiani systemd[1]: Started Journal Service.
Jun 24 08:48:38 galelhiani kernel: EXT4-fs (dm-0): re-mounted. Opts: (null). Quota mode: none.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Huge Pages File System.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted POSIX Message Queue File System.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Kernel Debug File System.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Kernel Trace File System.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Create List of Static Device Nodes.
Jun 24 08:48:38 galelhiani systemd[1]: modprobe@configfs.service: Deactivated successfully.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load Kernel Module configfs.
Jun 24 08:48:38 galelhiani systemd[1]: modprobe@drm.service: Deactivated successfully.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load Kernel Module drm.
Jun 24 08:48:38 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 08:48:38 galelhiani systemd[1]: modprobe@fuse.service: Deactivated successfully.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load Kernel Module fuse.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load Kernel Modules.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Remount Root and Kernel File Systems.
Jun 24 08:48:38 galelhiani systemd[1]: Activating swap /swap.img...
Jun 24 08:48:38 galelhiani kernel: Adding 4194300k swap on /swap.img.  Priority:-2 extents:3 across:4464636k FS
Jun 24 08:48:38 galelhiani systemd[1]: Mounting FUSE Control File System...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Kernel Configuration File System...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Device-Mapper Multipath Device Controller...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Flush Journal to Persistent Storage...
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load/Save Random Seed...
Jun 24 08:48:38 galelhiani systemd-journald[474]: Time spent on flushing to /var/log/journal/1955aac654704d37a292a15c85e64c9d is 1.641ms for 575 entries.
Jun 24 08:48:38 galelhiani systemd-journald[474]: System Journal (/var/log/journal/1955aac654704d37a292a15c85e64c9d) is 136.0M, max 4.0G, 3.8G free.
Jun 24 08:48:38 galelhiani kernel: alua: device handler registered
Jun 24 08:48:38 galelhiani kernel: emc: device handler registered
Jun 24 08:48:38 galelhiani kernel: rdac: device handler registered
Jun 24 08:48:38 galelhiani systemd[1]: Starting Apply Kernel Variables...
Jun 24 08:48:38 galelhiani systemd[1]: Starting Create System Users...
Jun 24 08:48:38 galelhiani systemd[1]: Activated swap /swap.img.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Set the console keyboard layout.
Jun 24 08:48:38 galelhiani multipathd[512]: --------start up--------
Jun 24 08:48:38 galelhiani multipathd[512]: read /etc/multipath.conf
Jun 24 08:48:38 galelhiani multipathd[512]: path checkers start up
Jun 24 08:48:38 galelhiani systemd[1]: Finished Coldplug All udev Devices.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted FUSE Control File System.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Kernel Configuration File System.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Apply Kernel Variables.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load/Save Random Seed.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in First Boot Complete being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Swaps.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Create System Users.
Jun 24 08:48:38 galelhiani systemd[1]: Starting Create Static Device Nodes in /dev...
Jun 24 08:48:38 galelhiani systemd[1]: Finished Create Static Device Nodes in /dev.
Jun 24 08:48:38 galelhiani systemd[1]: Starting Rule-based Manager for Device Events and Files...
Jun 24 08:48:38 galelhiani systemd[1]: Started Device-Mapper Multipath Device Controller.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Preparation for Local File Systems.
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for bare, revision 5...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for core20, revision 2321...
Jun 24 08:48:38 galelhiani kernel: loop0: detected capacity change from 0 to 8
Jun 24 08:48:38 galelhiani kernel: loop1: detected capacity change from 0 to 122368
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for core20, revision 2870...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for core24, revision 1644...
Jun 24 08:48:38 galelhiani kernel: loop2: detected capacity change from 0 to 122008
Jun 24 08:48:38 galelhiani kernel: loop3: detected capacity change from 0 to 126688
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for firefox, revision 8386...
Jun 24 08:48:38 galelhiani kernel: loop4: detected capacity change from 0 to 483496
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for firefox, revision 8416...
Jun 24 08:48:38 galelhiani kernel: loop5: detected capacity change from 0 to 483616
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for gnome-46-2404, revision 154...
Jun 24 08:48:38 galelhiani kernel: loop6: detected capacity change from 0 to 1132440
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for gtk-common-themes, revision 1535...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for lxd, revision 29353...
Jun 24 08:48:38 galelhiani kernel: loop7: detected capacity change from 0 to 187776
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for lxd, revision 38801...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for mesa-2404, revision 1166...
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for mesa-2404, revision 1778...
Jun 24 08:48:38 galelhiani kernel: loop8: detected capacity change from 0 to 158472
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for snapd, revision 21761...
Jun 24 08:48:38 galelhiani kernel: loop10: detected capacity change from 0 to 357512
Jun 24 08:48:38 galelhiani systemd[1]: Mounting Mount unit for snapd, revision 26869...
Jun 24 08:48:38 galelhiani systemd[1]: Started Rule-based Manager for Device Events and Files.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Flush Journal to Persistent Storage.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for bare, revision 5.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for core20, revision 2321.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for core20, revision 2870.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for core24, revision 1644.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for firefox, revision 8386.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for firefox, revision 8416.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for gnome-46-2404, revision 154.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for gtk-common-themes, revision 1535.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for lxd, revision 29353.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for lxd, revision 38801.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for mesa-2404, revision 1166.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for mesa-2404, revision 1778.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for snapd, revision 21761.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Local Encrypted Volumes.
Jun 24 08:48:38 galelhiani systemd[1]: Mounted Mount unit for snapd, revision 26869.
Jun 24 08:48:38 galelhiani systemd[1]: Reached target Mounted snaps.
Jun 24 08:48:38 galelhiani systemd-udevd[546]: Using default interface naming scheme 'v249'.
Jun 24 08:48:38 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 08:48:38 galelhiani mtp-probe[568]: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:0e.0/usb1/1-2"
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in OpenVSwitch configuration for cleanup being skipped.
Jun 24 08:48:38 galelhiani mtp-probe[568]: bus: 1, device: 3 was not an MTP device
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
Jun 24 08:48:38 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 08:48:38 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 08:48:38 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 08:48:38 galelhiani mtp-probe[571]: checking bus 1, device 2: "/sys/devices/pci0000:00/0000:00:0e.0/usb1/1-1"
Jun 24 08:48:38 galelhiani mtp-probe[577]: checking bus 4, device 2: "/sys/devices/pci0000:00/0000:00:0f.0/usb4/4-1"
Jun 24 08:48:38 galelhiani mtp-probe[571]: bus: 1, device: 2 was not an MTP device
Jun 24 08:48:38 galelhiani mtp-probe[577]: bus: 4, device: 2 was not an MTP device
Jun 24 08:48:38 galelhiani kernel: usbcore: registered new device driver apple-mfi-fastcharge
Jun 24 08:48:38 galelhiani kernel: virtiofs virtio2: virtio_fs_setup_dax: No cache capability
Jun 24 08:48:38 galelhiani kernel: virtiofs virtio3: virtio_fs_setup_dax: No cache capability
Jun 24 08:48:38 galelhiani systemd[1]: Found device /dev/disk/by-uuid/1B0A-2B4E.
Jun 24 08:48:38 galelhiani systemd[1]: Created slice Slice /system/lvm2-pvscan.
Jun 24 08:48:38 galelhiani systemd[1]: Starting LVM event activation on device 252:3...
Jun 24 08:48:38 galelhiani systemd[1]: Starting File System Check on /dev/disk/by-uuid/1B0A-2B4E...
Jun 24 08:48:38 galelhiani systemd[1]: Found device /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873.
Jun 24 08:48:38 galelhiani lvm[602]:   pvscan[602] PV /dev/vda3 online, VG ubuntu-vg is complete.
Jun 24 08:48:38 galelhiani lvm[602]:   pvscan[602] VG ubuntu-vg skip autoactivation.
Jun 24 08:48:38 galelhiani systemd-fsck[615]: fsck.fat 4.2 (2021-01-31)
Jun 24 08:48:38 galelhiani systemd-fsck[615]: There are differences between boot sector and its backup.
Jun 24 08:48:38 galelhiani systemd-fsck[615]: This is mostly harmless. Differences: (offset:original/backup)
Jun 24 08:48:38 galelhiani systemd-fsck[615]:   65:01/00
Jun 24 08:48:38 galelhiani systemd-fsck[615]:   Not automatically fixing this.
Jun 24 08:48:38 galelhiani systemd-fsck[615]: Dirty bit is set. Fs was not properly unmounted and some data may be corrupt.
Jun 24 08:48:38 galelhiani systemd-fsck[615]:  Automatically removing dirty bit.
Jun 24 08:48:38 galelhiani systemd-fsck[615]: *** Filesystem was changed ***
Jun 24 08:48:38 galelhiani systemd-fsck[615]: Writing changes.
Jun 24 08:48:38 galelhiani systemd-fsck[615]: /dev/vda1: 11 files, 1617/274658 clusters
Jun 24 08:48:38 galelhiani systemd[1]: Finished File System Check on /dev/disk/by-uuid/1B0A-2B4E.
Jun 24 08:48:38 galelhiani systemd[1]: Starting File System Check on /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873...
Jun 24 08:48:38 galelhiani systemd[1]: Started File System Check Daemon to report status.
Jun 24 08:48:38 galelhiani systemd-fsck[625]: /dev/vda2: recovering journal
Jun 24 08:48:38 galelhiani systemd[1]: Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
Jun 24 08:48:38 galelhiani systemd-fsck[625]: /dev/vda2: clean, 260/131072 files, 91148/524288 blocks
Jun 24 08:48:38 galelhiani systemd[1]: Finished LVM event activation on device 252:3.
Jun 24 08:48:38 galelhiani systemd[1]: Finished File System Check on /dev/disk/by-uuid/ee2146c8-069d-4b04-9520-7d50b84e6873.
Jun 24 08:48:38 galelhiani systemd[1]: Mounting /boot...
Jun 24 08:48:39 galelhiani systemd[1]: Mounted /boot.
Jun 24 08:48:39 galelhiani kernel: EXT4-fs (vda2): mounted filesystem with ordered data mode. Opts: (null). Quota mode: none.
Jun 24 08:48:39 galelhiani systemd[1]: Mounting /boot/efi...
Jun 24 08:48:39 galelhiani systemd[1]: Mounted /boot/efi.
Jun 24 08:48:39 galelhiani systemd[1]: Reached target Local File Systems.
Jun 24 08:48:39 galelhiani systemd[1]: Starting Load AppArmor profiles...
Jun 24 08:48:39 galelhiani systemd[1]: Starting Set console font and keymap...
Jun 24 08:48:39 galelhiani apparmor.systemd[725]: Restarting AppArmor
Jun 24 08:48:39 galelhiani apparmor.systemd[725]: Reloading AppArmor profiles
Jun 24 08:48:39 galelhiani systemd[1]: Starting Create final runtime dir for shutdown pivot root...
Jun 24 08:48:39 galelhiani systemd[1]: Starting Tell Plymouth To Write Out Runtime Data...
Jun 24 08:48:39 galelhiani systemd[1]: Starting Set Up Additional Binary Formats...
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Starting Create Volatile Files and Directories...
Jun 24 08:48:39 galelhiani systemd[1]: Starting Uncomplicated firewall...
Jun 24 08:48:39 galelhiani systemd[1]: Finished Set console font and keymap.
Jun 24 08:48:39 galelhiani systemd[1]: Finished Create final runtime dir for shutdown pivot root.
Jun 24 08:48:39 galelhiani systemd[1]: Finished Uncomplicated firewall.
Jun 24 08:48:39 galelhiani systemd[1]: proc-sys-fs-binfmt_misc.automount: Got automount request for /proc/sys/fs/binfmt_misc, triggered by 752 (systemd-binfmt)
Jun 24 08:48:39 galelhiani systemd[1]: Mounting Arbitrary Executable File Formats File System...
Jun 24 08:48:39 galelhiani audit[754]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=754 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.032:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=754 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[755]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=755 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[755]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=755 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.036:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe" pid=755 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.036:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="nvidia_modprobe//kmod" pid=755 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[765]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=765 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[765]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=765 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[765]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=765 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[757]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[757]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[757]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[757]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/{,usr/}sbin/dhclient" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[767]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="tcpdump" pid=767 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Finished Tell Plymouth To Write Out Runtime Data.
Jun 24 08:48:39 galelhiani systemd[1]: Finished Create Volatile Files and Directories.
Jun 24 08:48:39 galelhiani audit[769]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oosplash" pid=769 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.040:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=765 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.040:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=765 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.040:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=765 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.040:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.040:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani kernel: audit: type=1400 audit(1782290919.040:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=757 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[770]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=770 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Mounted Arbitrary Executable File Formats File System.
Jun 24 08:48:39 galelhiani audit[772]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=772 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Starting Userspace Out-Of-Memory (OOM) Killer...
Jun 24 08:48:39 galelhiani audit[774]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=774 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[773]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=773 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani apparmor.systemd[777]: Skipping profile in /etc/apparmor.d/disable: usr.sbin.rsyslogd
Jun 24 08:48:39 galelhiani apparmor.systemd[778]: Warning: found usr.sbin.sssd in /etc/apparmor.d/force-complain, forcing complain mode
Jun 24 08:48:39 galelhiani audit[758]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_apt_news" pid=758 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//apt_methods" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//apt_methods_gpgv" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//cloud_id" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//dpkg" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//ps" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache//ubuntu_distro_info" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache_systemctl" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[759]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="ubuntu_pro_esm_cache_systemd_detect_virt" pid=759 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[776]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/cups/backend/cups-pdf" pid=776 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[776]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cupsd" pid=776 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[776]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cupsd//third_party" pid=776 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Starting Network Time Synchronization...
Jun 24 08:48:39 galelhiani systemd[1]: Starting Record System Boot/Shutdown in UTMP...
Jun 24 08:48:39 galelhiani systemd[1]: Finished Set Up Additional Binary Formats.
Jun 24 08:48:39 galelhiani audit[760]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince" pid=760 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[760]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//sanitized_helper" pid=760 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[760]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince//snap_browsers" pid=760 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[760]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer" pid=760 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[760]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-previewer//sanitized_helper" pid=760 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[760]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/evince-thumbnailer" pid=760 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Finished Record System Boot/Shutdown in UTMP.
Jun 24 08:48:39 galelhiani audit[778]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/sssd" pid=778 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani apparmor.systemd[778]: Warning from /etc/apparmor.d (/etc/apparmor.d/usr.sbin.sssd line 69): Caching disabled for: 'usr.sbin.sssd' due to force complain
Jun 24 08:48:39 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in OpenVSwitch configuration for cleanup being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 08:48:39 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 08:48:39 galelhiani audit[771]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice" pid=771 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[771]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-soffice//gpg" pid=771 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Finished Load AppArmor profiles.
Jun 24 08:48:39 galelhiani systemd[1]: Starting Load AppArmor profiles managed internally by snapd...
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Authentication service for virtual machines hosted on VMware being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Condition check resulted in Service for virtual machines hosted on VMware being skipped.
Jun 24 08:48:39 galelhiani systemd[1]: Starting Cloud-init: Local Stage (pre-network)...
Jun 24 08:48:39 galelhiani snapd-apparmor[783]: main.go:146: Loading profiles [/var/lib/snapd/apparmor/profiles/snap-confine.snapd.21761 /var/lib/snapd/apparmor/profiles/snap-confine.snapd.26869 /var/lib/snapd/apparmor/profiles/snap-update-ns.firefox /var/lib/snapd/apparmor/profiles/snap-update-ns.lxd /var/lib/snapd/apparmor/profiles/snap-update-ns.mesa-2404 /var/lib/snapd/apparmor/profiles/snap.firefox.firefox /var/lib/snapd/apparmor/profiles/snap.firefox.geckodriver /var/lib/snapd/apparmor/profiles/snap.firefox.hook.configure /var/lib/snapd/apparmor/profiles/snap.firefox.hook.disconnect-plug-host-hunspell /var/lib/snapd/apparmor/profiles/snap.firefox.hook.install /var/lib/snapd/apparmor/profiles/snap.firefox.hook.post-refresh /var/lib/snapd/apparmor/profiles/snap.lxd.activate /var/lib/snapd/apparmor/profiles/snap.lxd.benchmark /var/lib/snapd/apparmor/profiles/snap.lxd.buginfo /var/lib/snapd/apparmor/profiles/snap.lxd.check-kernel /var/lib/snapd/apparmor/profiles/snap.lxd.daemon /var/lib/snapd/apparmor/profiles/snap.lxd.hook.configure /var/lib/snapd/apparmor/profiles/snap.lxd.hook.install /var/lib/snapd/apparmor/profiles/snap.lxd.hook.remove /var/lib/snapd/apparmor/profiles/snap.lxd.lxc /var/lib/snapd/apparmor/profiles/snap.lxd.lxc-to-lxd /var/lib/snapd/apparmor/profiles/snap.lxd.lxd /var/lib/snapd/apparmor/profiles/snap.lxd.migrate /var/lib/snapd/apparmor/profiles/snap.lxd.user-daemon /var/lib/snapd/apparmor/profiles/snap.mesa-2404.component-monitor /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.connect-plug-kernel-gpu-2404 /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.disconnect-plug-kernel-gpu-2404 /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.install /var/lib/snapd/apparmor/profiles/snap.mesa-2404.hook.post-refresh]
Jun 24 08:48:39 galelhiani audit[795]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.lxd" pid=795 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[793]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/26869/usr/lib/snapd/snap-confine" pid=793 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[792]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/21761/usr/lib/snapd/snap-confine" pid=792 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[792]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="/snap/snapd/21761/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=792 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[796]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.mesa-2404" pid=796 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[794]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap-update-ns.firefox" pid=794 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[800]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.disconnect-plug-host-hunspell" pid=800 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[802]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.post-refresh" pid=802 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[801]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.install" pid=801 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Started Network Time Synchronization.
Jun 24 08:48:39 galelhiani systemd[1]: Started Userspace Out-Of-Memory (OOM) Killer.
Jun 24 08:48:39 galelhiani systemd[1]: Reached target System Time Set.
Jun 24 08:48:39 galelhiani audit[797]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.firefox" pid=797 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[804]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.activate" pid=804 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[798]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.geckodriver" pid=798 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[805]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.benchmark" pid=805 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[806]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.buginfo" pid=806 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[807]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.check-kernel" pid=807 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[799]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.firefox.hook.configure" pid=799 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[810]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.hook.install" pid=810 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[808]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.daemon" pid=808 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[812]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.lxc" pid=812 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[811]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.hook.remove" pid=811 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[813]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.lxc-to-lxd" pid=813 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[809]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.hook.configure" pid=809 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[819]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.disconnect-plug-kernel-gpu-2404" pid=819 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[815]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.migrate" pid=815 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[817]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.component-monitor" pid=817 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[814]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.lxd" pid=814 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[816]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.lxd.user-daemon" pid=816 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[818]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.connect-plug-kernel-gpu-2404" pid=818 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[820]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.install" pid=820 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani audit[821]: AVC apparmor="STATUS" operation="profile_load" profile="unconfined" name="snap.mesa-2404.hook.post-refresh" pid=821 comm="apparmor_parser"
Jun 24 08:48:39 galelhiani systemd[1]: Finished Load AppArmor profiles managed internally by snapd.
Jun 24 08:48:39 galelhiani cloud-init[825]: Cloud-init v. 26.1-0ubuntu1~22.04.1 running 'init-local' at Wed, 24 Jun 2026 08:48:39 +0000. Up 2.97 seconds.
Jun 24 08:48:39 galelhiani systemd[1]: Finished Cloud-init: Local Stage (pre-network).
Jun 24 08:48:39 galelhiani systemd[1]: Reached target Preparation for Network.
Jun 24 08:48:39 galelhiani systemd[1]: Starting Network Configuration...
Jun 24 08:48:39 galelhiani systemd-networkd[828]: lo: Link UP
Jun 24 08:48:39 galelhiani systemd-networkd[828]: lo: Gained carrier
Jun 24 08:48:39 galelhiani systemd-networkd[828]: Enumeration completed
Jun 24 08:48:39 galelhiani systemd[1]: Started Network Configuration.
Jun 24 08:48:39 galelhiani systemd[1]: Starting Wait for Network to be Configured...
Jun 24 08:48:39 galelhiani systemd-networkd[828]: enp0s1: Link UP
Jun 24 08:48:39 galelhiani systemd[1]: Starting Network Name Resolution...
Jun 24 08:48:39 galelhiani systemd-resolved[830]: Positive Trust Anchors:
Jun 24 08:48:39 galelhiani systemd-resolved[830]: . IN DS 20326 8 2 e06d44b80b8f1d39a95c0b0d7c65d08458e880409bbc683457104237c7f8ec8d
Jun 24 08:48:39 galelhiani systemd-resolved[830]: Negative trust anchors: home.arpa 10.in-addr.arpa 16.172.in-addr.arpa 17.172.in-addr.arpa 18.172.in-addr.arpa 19.172.in-addr.arpa 20.172.in-addr.arpa 21.172.in-addr.arpa 22.172.in-addr.arpa 23.172.in-addr.arpa 24.172.in-addr.arpa 25.172.in-addr.arpa 26.172.in-addr.arpa 27.172.in-addr.arpa 28.172.in-addr.arpa 29.172.in-addr.arpa 30.172.in-addr.arpa 31.172.in-addr.arpa 168.192.in-addr.arpa d.f.ip6.arpa corp home internal intranet lan local private test
Jun 24 08:48:39 galelhiani systemd-resolved[830]: Using system hostname 'galelhiani'.
Jun 24 08:48:39 galelhiani systemd[1]: Started Network Name Resolution.
Jun 24 08:48:39 galelhiani systemd[1]: Reached target Host and Network Name Lookups.
Jun 24 08:48:39 galelhiani systemd-networkd[828]: enp0s1: Gained carrier
Jun 24 08:48:39 galelhiani systemd-networkd[828]: enp0s1: DHCPv4 address 192.168.64.2/24 via 192.168.64.1
Jun 24 08:48:39 galelhiani systemd-timesyncd[779]: Network configuration changed, trying to establish connection.
Jun 24 08:48:40 galelhiani systemd[1]: Starting Load Kernel Module efi_pstore...
Jun 24 08:48:40 galelhiani systemd[1]: Condition check resulted in Show Plymouth Boot Screen being skipped.
Jun 24 08:48:40 galelhiani systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
Jun 24 08:48:40 galelhiani systemd[1]: Condition check resulted in Store a System Token in an EFI Variable being skipped.
Jun 24 08:48:40 galelhiani systemd[1]: Condition check resulted in Commit a transient machine-id on disk being skipped.
Jun 24 08:48:40 galelhiani systemd[1]: modprobe@efi_pstore.service: Deactivated successfully.
Jun 24 08:48:40 galelhiani systemd[1]: Finished Load Kernel Module efi_pstore.
Jun 24 08:48:40 galelhiani systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
Jun 24 08:48:41 galelhiani systemd-networkd[828]: enp0s1: Gained IPv6LL
Jun 24 08:48:41 galelhiani systemd-timesyncd[779]: Network configuration changed, trying to establish connection.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Wait for Network to be Configured.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Cloud-init: Network Stage...
Jun 24 08:48:41 galelhiani cloud-init[837]: Cloud-init v. 26.1-0ubuntu1~22.04.1 running 'init' at Wed, 24 Jun 2026 08:48:41 +0000. Up 5.00 seconds.
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +++++++++++++++++++++++++++++++++++++++Net device info+++++++++++++++++++++++++++++++++++++++
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +--------+------+------------------------------+---------------+--------+-------------------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: | Device |  Up  |           Address            |      Mask     | Scope  |     Hw-Address    |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +--------+------+------------------------------+---------------+--------+-------------------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: | enp0s1 | True |         192.168.64.2         | 255.255.255.0 | global | 7a:e6:46:77:bc:66 |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: | enp0s1 | True | fe80::78e6:46ff:fe77:bc66/64 |       .       |  link  | 7a:e6:46:77:bc:66 |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   lo   | True |          127.0.0.1           |   255.0.0.0   |  host  |         .         |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   lo   | True |           ::1/128            |       .       |  host  |         .         |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +--------+------+------------------------------+---------------+--------+-------------------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +++++++++++++++++++++++++++++++Route IPv4 info+++++++++++++++++++++++++++++++
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +-------+--------------+--------------+-----------------+-----------+-------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: | Route | Destination  |   Gateway    |     Genmask     | Interface | Flags |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +-------+--------------+--------------+-----------------+-----------+-------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   0   |   0.0.0.0    | 192.168.64.1 |     0.0.0.0     |   enp0s1  |   UG  |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   1   | 192.168.64.0 |   0.0.0.0    |  255.255.255.0  |   enp0s1  |   U   |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   2   | 192.168.64.1 |   0.0.0.0    | 255.255.255.255 |   enp0s1  |   UH  |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +-------+--------------+--------------+-----------------+-----------+-------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +++++++++++++++++++Route IPv6 info+++++++++++++++++++
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +-------+-------------+---------+-----------+-------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: | Route | Destination | Gateway | Interface | Flags |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +-------+-------------+---------+-----------+-------+
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   1   |  fe80::/64  |    ::   |   enp0s1  |   U   |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   3   |    local    |    ::   |   enp0s1  |   U   |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: |   4   |  multicast  |    ::   |   enp0s1  |   U   |
Jun 24 08:48:41 galelhiani cloud-init[837]: ci-info: +-------+-------------+---------+-----------+-------+
Jun 24 08:48:41 galelhiani systemd[1]: Finished Cloud-init: Network Stage.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Cloud-config availability.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target System Initialization.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Process error reports when automatic reporting is enabled (file watch) being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Started CUPS Scheduler.
Jun 24 08:48:41 galelhiani systemd[1]: Started Start whoopsie on modification of the /var/crash directory.
Jun 24 08:48:41 galelhiani systemd[1]: Started Trigger anacron every hour.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Process error reports when automatic reporting is enabled (timer based) being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Started Daily apt download activities.
Jun 24 08:48:41 galelhiani systemd[1]: Started Daily apt upgrade and clean activities.
Jun 24 08:48:41 galelhiani systemd[1]: Started Daily dpkg database backup timer.
Jun 24 08:48:41 galelhiani systemd[1]: Started Periodic ext4 Online Metadata Check for All Filesystems.
Jun 24 08:48:41 galelhiani systemd[1]: Started Discard unused blocks once a week.
Jun 24 08:48:41 galelhiani systemd[1]: Started Refresh fwupd metadata regularly.
Jun 24 08:48:41 galelhiani systemd[1]: Started Daily rotation of log files.
Jun 24 08:48:41 galelhiani systemd[1]: Started Daily man-db regeneration.
Jun 24 08:48:41 galelhiani systemd[1]: Started Message of the Day.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Timer to automatically fetch and run repair assertions being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Started Daily Cleanup of Temporary Directories.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Ubuntu Pro Timer for running repeated jobs being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Path Units.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Unix socket for apport crash forwarding being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on cloud-init hotplug hook socket.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on CUPS Scheduler.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on D-Bus System Message Bus Socket.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on Open-iSCSI iscsid Socket.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on Socket unix for snap application lxd.daemon.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on Socket unix for snap application lxd.user-daemon.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Socket activation for snappy daemon...
Jun 24 08:48:41 galelhiani systemd[1]: Listening on Activation socket for spice guest agent daemon.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on UUID daemon activation socket.
Jun 24 08:48:41 galelhiani systemd[1]: Listening on Socket activation for snappy daemon.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Socket Units.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Basic System.
Jun 24 08:48:41 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 08:48:41 galelhiani anacron[842]: Anacron 2.3 started on 2026-06-24
Jun 24 08:48:41 galelhiani systemd[1]: Starting Avahi mDNS/DNS-SD Stack...
Jun 24 08:48:41 galelhiani systemd[1]: Started D-Bus System Message Bus.
Jun 24 08:48:41 galelhiani anacron[842]: Normal exit (0 jobs run)
Jun 24 08:48:41 galelhiani systemd[1]: Starting Network Manager...
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Found user 'avahi' (UID 121) and group 'avahi' (GID 127).
Jun 24 08:48:41 galelhiani systemd[1]: Started Save initial kernel messages after boot.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Remove Stale Online ext4 Metadata Check Snapshots...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in getty on tty2-tty6 if dbus and logind are not available being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Login Prompts.
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] AppArmor D-Bus mediation is enabled
Jun 24 08:48:41 galelhiani systemd[1]: Starting Record successful boot for GRUB...
Jun 24 08:48:41 galelhiani systemd[1]: Started irqbalance daemon.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.4364] NetworkManager (version 1.36.6) is starting... (for the first time)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.4365] Read config: /etc/NetworkManager/NetworkManager.conf (lib: 10-default-firewall-use-iptables.conf, 10-dns-resolved.conf, 10-globally-managed-devices.conf, 20-connectivity-ubuntu.conf, no-mac-addr-change.conf) (etc: default-wifi-powersave-on.conf)
Jun 24 08:48:41 galelhiani systemd[1]: Starting Dispatcher daemon for systemd-networkd...
Jun 24 08:48:41 galelhiani systemd[1]: Starting Authorization Manager...
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.4393] bus-manager: acquired D-Bus service "org.freedesktop.NetworkManager"
Jun 24 08:48:41 galelhiani systemd[1]: Starting Power Profiles daemon...
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ vgic(9) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ arch_timer(10) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ vtimer(11) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ arm-pmu(14) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ ACPI:Event(15) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio8-config(26) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio8-inflate(27) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio8-deflate(28) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio9-config(29) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio9-input(30) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio9-output(31) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio9-control-i(32) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio1-config(33) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio1-req.0(34) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio0-config(35) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio0-input.0(36) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio0-output.0(37) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio7-config(38) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio7-input(39) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(41) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(42) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(43) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(44) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(45) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(46) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(47) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(49) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(50) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(51) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(52) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(53) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(54) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ xhci_hcd(55) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio4-config(56) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio4-control(57) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio4-cursor(58) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio2-config(59) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio2-hiprio(60) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio2-requests.0(61) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio3-config(62) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio3-hiprio(63) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio3-requests.0(64) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio5-config(65) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio5-virtsnd-ctl(66) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio5-virtsnd-event(67) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio5-virtsnd-tx(68) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio5-virtsnd-rx(69) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio6-config(70) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio6-virtsnd-ctl(71) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio6-virtsnd-event(72) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio6-virtsnd-tx(73) guessed as class 0
Jun 24 08:48:41 galelhiani /usr/sbin/irqbalance[851]: IRQ virtio6-virtsnd-rx(74) guessed as class 0
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.4428] manager[0xaaaaf8a84030]: monitoring kernel firmware directory '/lib/firmware'.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.4428] monitoring ifupdown state file '/run/network/ifstate'.
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Activating systemd to hand-off: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.4' (uid=0 pid=845 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 24 08:48:41 galelhiani polkitd[854]: started daemon version 0.105 using authority implementation `local' version `0.105'
Jun 24 08:48:41 galelhiani systemd[1]: Starting System Logging Service...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Secure Boot updates for DB and DBX being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Automatically repair incorrect owner/permissions on core devices being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Wait for the Ubuntu Core chooser trigger being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Preparation for Logins.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Wait until snapd is fully seeded...
Jun 24 08:48:41 galelhiani systemd[1]: Starting Snap Daemon...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in System Security Services Daemon being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target User and Group Name Lookups.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-nss.socket: Bound to unit sssd.service, but unit isn't active.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD NSS Service responder socket.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-nss.socket: Job sssd-nss.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-autofs.socket: Bound to unit sssd.service, but unit isn't active.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD AutoFS Service responder socket.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-autofs.socket: Job sssd-autofs.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-pac.socket: Bound to unit sssd.service, but unit isn't active.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD PAC Service responder socket.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-pac.socket: Job sssd-pac.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-pam-priv.socket: Bound to unit sssd.service, but unit isn't active.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD PAM Service responder private socket.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD PAM Service responder socket.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-pam.socket: Job sssd-pam.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-pam-priv.socket: Job sssd-pam-priv.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-ssh.socket: Bound to unit sssd.service, but unit isn't active.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD SSH Service responder socket.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-ssh.socket: Job sssd-ssh.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-sudo.socket: Bound to unit sssd.service, but unit isn't active.
Jun 24 08:48:41 galelhiani systemd[1]: Dependency failed for SSSD Sudo Service responder socket.
Jun 24 08:48:41 galelhiani systemd[1]: sssd-sudo.socket: Job sssd-sudo.socket/start failed with result 'dependency'.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Accounts Service...
Jun 24 08:48:41 galelhiani systemd[1]: Starting Switcheroo Control Proxy service...
Jun 24 08:48:41 galelhiani systemd[1]: Starting User Login Management...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Ubuntu Pro reboot cmds being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Disk Manager...
Jun 24 08:48:41 galelhiani systemd[1]: Starting WPA supplicant...
Jun 24 08:48:41 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani systemd[1]: e2scrub_reap.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Remove Stale Online ext4 Metadata Check Snapshots.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Successfully dropped root privileges.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: avahi-daemon 0.8 starting up.
Jun 24 08:48:41 galelhiani udisksd[884]: udisks daemon version 2.9.4 starting
Jun 24 08:48:41 galelhiani systemd[1]: Started Switcheroo Control Proxy service.
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.systemd1'
Jun 24 08:48:41 galelhiani systemd[1]: Started Power Profiles daemon.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Successfully called chroot().
Jun 24 08:48:41 galelhiani systemd[1]: Started Network Manager.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Successfully dropped remaining capabilities.
Jun 24 08:48:41 galelhiani systemd[1]: Started Authorization Manager.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: No service file found in /etc/avahi/services.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Joining mDNS multicast group on interface enp0s1.IPv6 with address fe80::78e6:46ff:fe77:bc66.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: New relevant interface enp0s1.IPv6 for mDNS.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Joining mDNS multicast group on interface enp0s1.IPv4 with address 192.168.64.2.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: New relevant interface enp0s1.IPv4 for mDNS.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Joining mDNS multicast group on interface lo.IPv6 with address ::1.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: New relevant interface lo.IPv6 for mDNS.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Joining mDNS multicast group on interface lo.IPv4 with address 127.0.0.1.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: New relevant interface lo.IPv4 for mDNS.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Network interface enumeration completed.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Registering new address record for fe80::78e6:46ff:fe77:bc66 on enp0s1.*.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Registering new address record for 192.168.64.2 on enp0s1.IPv4.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Registering new address record for ::1 on lo.*.
Jun 24 08:48:41 galelhiani avahi-daemon[843]: Registering new address record for 127.0.0.1 on lo.IPv4.
Jun 24 08:48:41 galelhiani systemd[1]: Started Avahi mDNS/DNS-SD Stack.
Jun 24 08:48:41 galelhiani systemd[1]: Started WPA supplicant.
Jun 24 08:48:41 galelhiani wpa_supplicant[888]: Successfully initialized wpa_supplicant
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Network.
Jun 24 08:48:41 galelhiani rsyslogd[865]: imuxsock: Acquired UNIX socket '/run/systemd/journal/syslog' (fd 3) from systemd.  [v8.2112.0]
Jun 24 08:48:41 galelhiani systemd[1]: Starting Modem Manager...
Jun 24 08:48:41 galelhiani rsyslogd[865]: rsyslogd's groupid changed to 113
Jun 24 08:48:41 galelhiani systemd[1]: Starting Network Manager Wait Online...
Jun 24 08:48:41 galelhiani rsyslogd[865]: rsyslogd's userid changed to 106
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Manage Sound Card State (restore and store) being skipped.
Jun 24 08:48:41 galelhiani rsyslogd[865]: [origin software="rsyslogd" swVersion="8.2112.0" x-pid="865" x-info="https://www.rsyslog.com"] start
Jun 24 08:48:41 galelhiani systemd[1]: Starting Save/Restore Sound Card State...
Jun 24 08:48:41 galelhiani systemd[1]: Starting CUPS Scheduler...
Jun 24 08:48:41 galelhiani systemd[1]: Starting A high performance web server and a reverse proxy server...
Jun 24 08:48:41 galelhiani systemd[1]: Starting OpenVPN service...
Jun 24 08:48:41 galelhiani systemd-logind[883]: New seat seat0.
Jun 24 08:48:41 galelhiani ModemManager[898]: <info>  ModemManager (version 1.20.0) starting in system bus...
Jun 24 08:48:41 galelhiani udisksd[884]: failed to load module mdraid: libbd_mdraid.so.2: cannot open shared object file: No such file or directory
Jun 24 08:48:41 galelhiani systemd-logind[883]: Watching system buttons on /dev/input/event0 (Power Button)
Jun 24 08:48:41 galelhiani systemd-logind[883]: Watching system buttons on /dev/input/event1 (Apple Inc. Virtual USB Keyboard)
Jun 24 08:48:41 galelhiani systemd[1]: Starting Service for snap application lxd.activate...
Jun 24 08:48:41 galelhiani systemd[1]: Starting Hostname Service...
Jun 24 08:48:41 galelhiani systemd[1]: Started System Logging Service.
Jun 24 08:48:41 galelhiani systemd[1]: Finished OpenVPN service.
Jun 24 08:48:41 galelhiani alsactl[924]: alsa-lib main.c:1412:(snd_use_case_mgr_open) error: failed to import hw:0 use case configuration -2
Jun 24 08:48:41 galelhiani alsactl[924]: alsa-lib main.c:1412:(snd_use_case_mgr_open) error: failed to import hw:1 use case configuration -2
Jun 24 08:48:41 galelhiani systemd[1]: grub-common.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Record successful boot for GRUB.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Save/Restore Sound Card State.
Jun 24 08:48:41 galelhiani networkd-dispatcher[853]: No valid path found for iw
Jun 24 08:48:41 galelhiani udisksd[884]: Failed to load the 'mdraid' libblockdev plugin
Jun 24 08:48:41 galelhiani systemd[1]: Started User Login Management.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Sound Card.
Jun 24 08:48:41 galelhiani accounts-daemon[868]: started daemon version 22.07.5
Jun 24 08:48:41 galelhiani systemd[1]: Starting GRUB failed boot detection...
Jun 24 08:48:41 galelhiani audit[904]: AVC apparmor="DENIED" operation="capable" profile="/usr/sbin/cupsd" pid=904 comm="cupsd" capability=12  capname="net_admin"
Jun 24 08:48:41 galelhiani systemd[1]: Started Unattended Upgrades Shutdown.
Jun 24 08:48:41 galelhiani kernel: kauditd_printk_skb: 59 callbacks suppressed
Jun 24 08:48:41 galelhiani kernel: audit: type=1400 audit(1782290921.532:70): apparmor="DENIED" operation="capable" profile="/usr/sbin/cupsd" pid=904 comm="cupsd" capability=12  capname="net_admin"
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.hostname1'
Jun 24 08:48:41 galelhiani systemd[1]: Started Dispatcher daemon for systemd-networkd.
Jun 24 08:48:41 galelhiani systemd[1]: Started CUPS Scheduler.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5384] hostname: hostname: using hostnamed
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5384] hostname: static hostname changed from (none) to "galelhiani"
Jun 24 08:48:41 galelhiani systemd[1]: Started Accounts Service.
Jun 24 08:48:41 galelhiani systemd[1]: Started Hostname Service.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5409] dns-mgr[0xaaaaf8a602a0]: init: dns=systemd-resolved rc-manager=unmanaged (auto), plugin=systemd-resolved
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5415] manager[0xaaaaf8a84030]: rfkill: Wi-Fi hardware radio set enabled
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5416] manager[0xaaaaf8a84030]: rfkill: WWAN hardware radio set enabled
Jun 24 08:48:41 galelhiani systemd[1]: Started A high performance web server and a reverse proxy server.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5455] Loaded device plugin: NMWifiFactory (/usr/lib/aarch64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-wifi.so)
Jun 24 08:48:41 galelhiani systemd[1]: grub-initrd-fallback.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5460] Loaded device plugin: NMAtmManager (/usr/lib/aarch64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-adsl.so)
Jun 24 08:48:41 galelhiani systemd[1]: Finished GRUB failed boot detection.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5496] Loaded device plugin: NMBluezManager (/usr/lib/aarch64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-bluetooth.so)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5515] Loaded device plugin: NMTeamFactory (/usr/lib/aarch64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-team.so)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5524] Loaded device plugin: NMWwanFactory (/usr/lib/aarch64-linux-gnu/NetworkManager/1.36.6/libnm-device-plugin-wwan.so)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5527] manager: rfkill: Wi-Fi enabled by radio killswitch; enabled by state file
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5527] manager: rfkill: WWAN enabled by radio killswitch; enabled by state file
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5528] manager: Networking is enabled by state file
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.4' (uid=0 pid=845 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")
Jun 24 08:48:41 galelhiani systemd[1]: Starting Network Manager Script Dispatcher Service...
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5560] settings: Loaded settings plugin: ifupdown ("/usr/lib/aarch64-linux-gnu/NetworkManager/1.36.6/libnm-settings-plugin-ifupdown.so")
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5560] settings: Loaded settings plugin: keyfile (internal)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5560] ifupdown: management mode: unmanaged
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5560] ifupdown: interfaces file /etc/network/interfaces doesn't exist
Jun 24 08:48:41 galelhiani systemd[1]: Started Disk Manager.
Jun 24 08:48:41 galelhiani systemd[1]: Started Modem Manager.
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5607] dhcp-init: Using DHCP client 'internal'
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5607] device (lo): carrier: link connected
Jun 24 08:48:41 galelhiani udisksd[884]: Cleaning up mount point /media/galelhiani/Ubuntu-Server 22.04.5 LTS arm64 (device 8:1 is not mounted)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5609] manager: (lo): new Generic device (/org/freedesktop/NetworkManager/Devices/1)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5613] device (enp0s1): carrier: link connected
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5614] manager: (enp0s1): new Ethernet device (/org/freedesktop/NetworkManager/Devices/2)
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5631] failed to open /run/network/ifstate
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5640] manager: startup complete
Jun 24 08:48:41 galelhiani systemd[1]: Finished Network Manager Wait Online.
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Jun 24 08:48:41 galelhiani NetworkManager[845]: <info>  [1782290921.5663] modem-manager: ModemManager available
Jun 24 08:48:41 galelhiani systemd[1]: Started Network Manager Script Dispatcher Service.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Network is Online.
Jun 24 08:48:41 galelhiani systemd[1]: Started Download data for packages that failed at package install time.
Jun 24 08:48:41 galelhiani systemd[1]: Started Check to see whether there is a new version of Ubuntu available.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Timer Units.
Jun 24 08:48:41 galelhiani systemd[1]: Started Make remote CUPS printers available locally.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Samba NMB Daemon...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Login to default iSCSI targets being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Preparation for Remote File Systems.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Remote File Systems.
Jun 24 08:48:41 galelhiani systemd[1]: Starting LSB: automatic crash report generation...
Jun 24 08:48:41 galelhiani systemd[1]: Starting Deferred execution scheduler...
Jun 24 08:48:41 galelhiani systemd[1]: Finished Availability of block devices.
Jun 24 08:48:41 galelhiani systemd[1]: Started Regular background program processing daemon.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Tool to automatically collect and submit kernel crash signatures...
Jun 24 08:48:41 galelhiani cron[970]: (CRON) INFO (pidfile fd = 3)
Jun 24 08:48:41 galelhiani cron[970]: (CRON) INFO (Running @reboot jobs)
Jun 24 08:48:41 galelhiani udisksd[884]: Acquired the name org.freedesktop.UDisks2 on the system message bus
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Pollinate to seed the pseudo random number generator being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Starting OpenBSD Secure Shell server...
Jun 24 08:48:41 galelhiani systemd[1]: Starting Permit User Sessions...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Ubuntu Pro Background Auto Attach being skipped.
Jun 24 08:48:41 galelhiani systemd[1]: Started Deferred execution scheduler.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Permit User Sessions.
Jun 24 08:48:41 galelhiani systemd[1]: Starting GNOME Display Manager...
Jun 24 08:48:41 galelhiani audit[954]: AVC apparmor="DENIED" operation="capable" profile="/usr/sbin/cups-browsed" pid=954 comm="cups-browsed" capability=23  capname="sys_nice"
Jun 24 08:48:41 galelhiani systemd[1]: Starting Hold until boot process finishes up...
Jun 24 08:48:41 galelhiani kernel: audit: type=1400 audit(1782290921.612:71): apparmor="DENIED" operation="capable" profile="/usr/sbin/cups-browsed" pid=954 comm="cups-browsed" capability=23  capname="sys_nice"
Jun 24 08:48:41 galelhiani systemd[1]: kerneloops.service: Found left-over process 990 (kerneloops) in control group while starting unit. Ignoring.
Jun 24 08:48:41 galelhiani systemd[1]: This usually indicates unclean termination of a previous run, or service implementation deficiencies.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Hold until boot process finishes up.
Jun 24 08:48:41 galelhiani sshd[1011]: Server listening on 0.0.0.0 port 22.
Jun 24 08:48:41 galelhiani sshd[1011]: Server listening on :: port 22.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Set console scheme...
Jun 24 08:48:41 galelhiani apport[965]:  * Starting automatic crash report generation: apport
Jun 24 08:48:41 galelhiani snapd[867]: overlord.go:309: Acquiring state lock file
Jun 24 08:48:41 galelhiani snapd[867]: overlord.go:314: Acquired state lock file
Jun 24 08:48:41 galelhiani apport[965]:    ...done.
Jun 24 08:48:41 galelhiani systemd[1]: Started OpenBSD Secure Shell server.
Jun 24 08:48:41 galelhiani systemd[1]: Started LSB: automatic crash report generation.
Jun 24 08:48:41 galelhiani systemd[1]: Started Tool to automatically collect and submit kernel crash signatures.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Set console scheme.
Jun 24 08:48:41 galelhiani systemd[1]: Created slice Slice /system/getty.
Jun 24 08:48:41 galelhiani systemd[1]: Started crash report submission.
Jun 24 08:48:41 galelhiani snapd[867]: daemon.go:276: started snapd/2.75.2+ubuntu22.04 (series 16; classic) ubuntu/22.04 (arm64) linux/5.15.0-181-generic.
Jun 24 08:48:41 galelhiani systemd[1]: Started Samba NMB Daemon.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Samba SMB Daemon...
Jun 24 08:48:41 galelhiani systemd[1]: Started GNOME Display Manager.
Jun 24 08:48:41 galelhiani systemd[1]: tmp-syscheck\x2dmountpoint\x2d3901602036.mount: Deactivated successfully.
Jun 24 08:48:41 galelhiani whoopsie[1031]: [08:48:41] Using lock path: /var/lock/whoopsie/lock
Jun 24 08:48:41 galelhiani systemd[1]: whoopsie.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani snapd[867]: daemon.go:370: adjusting startup timeout by 1m15s (pessimistic estimate of 30s plus 5s per snap)
Jun 24 08:48:41 galelhiani snapd[867]: backends.go:70: AppArmor status: apparmor is enabled and all features are available
Jun 24 08:48:41 galelhiani snapd[867]: backend.go:145: reloading profiles for snap-confine
Jun 24 08:48:41 galelhiani systemd[1]: Started Samba SMB Daemon.
Jun 24 08:48:41 galelhiani lxd.activate[911]: => Starting LXD activation
Jun 24 08:48:41 galelhiani lxd.activate[911]: ==> Loading snap configuration
Jun 24 08:48:41 galelhiani lxd.activate[911]: ==> Checking for socket activation support
Jun 24 08:48:41 galelhiani audit[1071]: AVC apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=1071 comm="apparmor_parser"
Jun 24 08:48:41 galelhiani kernel: audit: type=1400 audit(1782290921.756:72): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=1071 comm="apparmor_parser"
Jun 24 08:48:41 galelhiani snapd[867]: standby.go:95: will consider standby after: 5s
Jun 24 08:48:41 galelhiani systemd[1]: Started Snap Daemon.
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.28' (uid=0 pid=867 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 24 08:48:41 galelhiani systemd[1]: Starting Time & Date Service...
Jun 24 08:48:41 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 24 08:48:41 galelhiani systemd[1]: Started Time & Date Service.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Wait until snapd is fully seeded.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Cloud-init: Config Stage...
Jun 24 08:48:41 galelhiani systemd[1]: Condition check resulted in Auto import assertions from block devices being skipped.
Jun 24 08:48:41 galelhiani lxd.activate[911]: ==> Setting LXD socket ownership
Jun 24 08:48:41 galelhiani lxd.activate[911]: ==> Setting LXD user socket ownership
Jun 24 08:48:41 galelhiani lxd.activate[911]: ==> LXD never started on this system, no need to start it now
Jun 24 08:48:41 galelhiani systemd[1]: snap.lxd.activate.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Service for snap application lxd.activate.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Multi-User System.
Jun 24 08:48:41 galelhiani systemd[1]: Reached target Graphical Interface.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Record Runlevel Change in UTMP...
Jun 24 08:48:41 galelhiani systemd[1]: systemd-update-utmp-runlevel.service: Deactivated successfully.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Record Runlevel Change in UTMP.
Jun 24 08:48:41 galelhiani cloud-init[1113]: Cloud-init v. 26.1-0ubuntu1~22.04.1 running 'modules:config' at Wed, 24 Jun 2026 08:48:41 +0000. Up 5.60 seconds.
Jun 24 08:48:41 galelhiani systemd[1]: Finished Cloud-init: Config Stage.
Jun 24 08:48:41 galelhiani systemd[1]: Starting Cloud-init: Final Stage...
Jun 24 08:48:42 galelhiani cloud-init[1118]: Cloud-init v. 26.1-0ubuntu1~22.04.1 running 'modules:final' at Wed, 24 Jun 2026 08:48:42 +0000. Up 5.71 seconds.
Jun 24 08:48:42 galelhiani cloud-init[1118]: Cloud-init v. 26.1-0ubuntu1~22.04.1 finished at Wed, 24 Jun 2026 08:48:42 +0000. Datasource DataSourceNone.  Up 5.73 seconds
Jun 24 08:48:42 galelhiani systemd[1]: Finished Cloud-init: Final Stage.
Jun 24 08:48:42 galelhiani systemd[1]: Reached target Cloud-init target.
Jun 24 08:48:42 galelhiani systemd[1]: Startup finished in 2.235s (kernel) + 3.515s (userspace) = 5.751s.
Jun 24 08:48:42 galelhiani systemd[1]: dmesg.service: Deactivated successfully.
Jun 24 08:48:42 galelhiani avahi-daemon[843]: Server startup complete. Host name is galelhiani.local. Local service cookie is 908775252.
Jun 24 08:48:42 galelhiani snapd[867]: snapmgr.go:1661: performing periodic snap downloads cache cleanup
Jun 24 08:48:42 galelhiani snapd[867]: cache.go:243: removed 0 entries/    0 from downloads cache
Jun 24 08:48:42 galelhiani avahi-daemon[843]: Leaving mDNS multicast group on interface enp0s1.IPv6 with address fe80::78e6:46ff:fe77:bc66.
Jun 24 08:48:42 galelhiani systemd-timesyncd[779]: Network configuration changed, trying to establish connection.
Jun 24 08:48:42 galelhiani avahi-daemon[843]: Joining mDNS multicast group on interface enp0s1.IPv6 with address fd2f:59a9:1813:5d8e:78e6:46ff:fe77:bc66.
Jun 24 08:48:42 galelhiani avahi-daemon[843]: Registering new address record for fd2f:59a9:1813:5d8e:78e6:46ff:fe77:bc66 on enp0s1.*.
Jun 24 08:48:42 galelhiani avahi-daemon[843]: Withdrawing address record for fe80::78e6:46ff:fe77:bc66 on enp0s1.
Jun 24 08:48:44 galelhiani ModemManager[898]: <info>  [base-manager] couldn't check support for device '/sys/devices/pci0000:00/0000:00:01.0': not supported by any plugin
Jun 24 08:48:44 galelhiani systemd-timesyncd[779]: Network configuration changed, trying to establish connection.
Jun 24 08:48:51 galelhiani systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Jun 24 08:48:52 galelhiani gdm-launch-environment][1151]: pam_unix(gdm-launch-environment:session): session opened for user gdm(uid=131) by (uid=0)
Jun 24 08:48:52 galelhiani systemd[1]: Created slice User Slice of UID 131.
Jun 24 08:48:52 galelhiani systemd[1]: Starting User Runtime Directory /run/user/131...
Jun 24 08:48:52 galelhiani systemd-logind[883]: New session c1 of user gdm.
Jun 24 08:48:52 galelhiani systemd[1]: Finished User Runtime Directory /run/user/131.
Jun 24 08:48:52 galelhiani systemd[1]: Starting User Manager for UID 131...
Jun 24 08:48:52 galelhiani systemd[1156]: pam_unix(systemd-user:session): session opened for user gdm(uid=131) by (uid=0)
Jun 24 08:48:52 galelhiani systemd[1156]: Queued start job for default target Main User Target.
Jun 24 08:48:52 galelhiani systemd[1156]: Created slice User Application Slice.
Jun 24 08:48:52 galelhiani systemd[1156]: Created slice User Core Session Slice.
Jun 24 08:48:52 galelhiani systemd[1156]: Started Pending report trigger for Ubuntu Report.
Jun 24 08:48:52 galelhiani systemd[1156]: Reached target Paths.
Jun 24 08:48:52 galelhiani systemd[1156]: Reached target Timers.
Jun 24 08:48:52 galelhiani systemd[1156]: Starting D-Bus User Message Bus Socket...
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on GnuPG network certificate management daemon.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on GnuPG cryptographic agent and passphrase cache.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on PipeWire Multimedia System Socket.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on debconf communication socket.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on Sound System.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on REST API socket for snapd user session agent.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on Speech Dispatcher Socket.
Jun 24 08:48:52 galelhiani systemd[1156]: Listening on D-Bus User Message Bus Socket.
Jun 24 08:48:52 galelhiani systemd[1156]: Reached target Sockets.
Jun 24 08:48:52 galelhiani systemd[1156]: Reached target Basic System.
Jun 24 08:48:52 galelhiani systemd[1]: Started User Manager for UID 131.
Jun 24 08:48:52 galelhiani systemd[1156]: Started PipeWire Multimedia Service.
Jun 24 08:48:52 galelhiani systemd[1]: Started Session c1 of User gdm.
Jun 24 08:48:52 galelhiani systemd[1156]: Started PipeWire Media Session Manager.
Jun 24 08:48:52 galelhiani systemd[1156]: Starting Sound Service...
Jun 24 08:48:52 galelhiani systemd[1156]: Started D-Bus User Message Bus.
Jun 24 08:48:52 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.RealtimeKit1' unit='rtkit-daemon.service' requested by ':1.33' (uid=131 pid=1164 comm="/usr/bin/pipewire-media-session " label="unconfined")
Jun 24 08:48:52 galelhiani systemd[1]: Starting RealtimeKit Scheduling Policy Service...
Jun 24 08:48:52 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.RealtimeKit1'
Jun 24 08:48:52 galelhiani systemd[1]: Started RealtimeKit Scheduling Policy Service.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully called chroot.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully dropped privileges.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully limited resources.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Running.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Canary thread running.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 0 threads of 0 processes of 0 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Watchdog thread running.
Jun 24 08:48:52 galelhiani dbus-daemon[1168]: [session uid=131 pid=1168] AppArmor D-Bus mediation is enabled
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully made thread 1163 of process 1163 owned by '131' high priority at nice level -11.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 1 threads of 1 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully made thread 1165 of process 1165 owned by '131' high priority at nice level -11.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 2 threads of 2 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 2 threads of 2 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 2 threads of 2 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully made thread 1172 of process 1164 owned by '131' RT at priority 20.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 3 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 3 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully made thread 1177 of process 1163 owned by '131' RT at priority 20.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 4 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 4 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully made thread 1180 of process 1165 owned by '131' RT at priority 5.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 5 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani gnome-session[1176]: gnome-session-binary[1176]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 24 08:48:52 galelhiani gnome-session[1176]: gnome-session-binary[1176]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 24 08:48:52 galelhiani gnome-session-binary[1176]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 24 08:48:52 galelhiani gnome-session-binary[1176]: GLib-GIO-CRITICAL: g_bus_get_sync: assertion 'error == NULL || *error == NULL' failed
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Running GNOME Shell (using mutter 42.9) as a Wayland display server
Jun 24 08:48:52 galelhiani pulseaudio[1165]: ALSA woke us up to read new data from the device, but there was actually nothing to read.
Jun 24 08:48:52 galelhiani pulseaudio[1165]: Most likely this is a bug in the ALSA driver 'virtio_snd'. Please report this issue to the ALSA developers.
Jun 24 08:48:52 galelhiani pulseaudio[1165]: We were woken up with POLLIN set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 5 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Successfully made thread 1188 of process 1165 owned by '131' RT at priority 5.
Jun 24 08:48:52 galelhiani rtkit-daemon[1169]: Supervising 6 threads of 3 processes of 1 users.
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Added device '/dev/dri/card0' (virtio_gpu) using non-atomic mode setting.
Jun 24 08:48:52 galelhiani pulseaudio[1165]: ALSA woke us up to write new data to the device, but there was actually nothing to write.
Jun 24 08:48:52 galelhiani pulseaudio[1165]: Most likely this is a bug in the ALSA driver 'virtio_snd'. Please report this issue to the ALSA developers.
Jun 24 08:48:52 galelhiani pulseaudio[1165]: We were woken up with POLLOUT set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 24 08:48:52 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.42' (uid=131 pid=1165 comm="/usr/bin/pulseaudio --daemonize=no --log-target=jo" label="unconfined")
Jun 24 08:48:52 galelhiani systemd[1]: Condition check resulted in Bluetooth service being skipped.
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Failed to initialize accelerated iGPU/dGPU framebuffer sharing: Not hardware accelerated
Jun 24 08:48:52 galelhiani systemd[1156]: Started Sound Service.
Jun 24 08:48:52 galelhiani systemd[1156]: Reached target Main User Target.
Jun 24 08:48:52 galelhiani systemd[1156]: Startup finished in 328ms.
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1184]: libEGL warning: egl: failed to create dri2 screen
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1184]: libEGL warning: NEEDS EXTENSION: falling back to kms_swrast
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Created gbm renderer for '/dev/dri/card0'
Jun 24 08:48:52 galelhiani gnome-shell[1184]: GPU /dev/dri/card0 selected as primary
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Disabling DMA buffer screen sharing (not hardware accelerated)
Jun 24 08:48:52 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.a11y.Bus' requested by ':1.4' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:52 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.a11y.Bus'
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Using public X11 display :1024, (using :1025 for managed services)
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Using Wayland display name 'wayland-0'
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1223]: (WW) Option "-listen" for file descriptors is deprecated
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1223]: Please use "-listenfd" instead.
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1223]: (WW) Option "-listen" for file descriptors is deprecated
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1223]: Please use "-listenfd" instead.
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1223]: libEGL warning: egl: failed to create dri2 screen
Jun 24 08:48:52 galelhiani org.gnome.Shell.desktop[1223]: libEGL warning: NEEDS EXTENSION: falling back to kms_swrast
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
Jun 24 08:48:52 galelhiani gnome-shell[1184]: Will monitor session c1
Jun 24 08:48:52 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.locale1' unit='dbus-org.freedesktop.locale1.service' requested by ':1.41' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:52 galelhiani systemd[1]: Starting Locale Service...
Jun 24 08:48:52 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.locale1'
Jun 24 08:48:52 galelhiani systemd[1]: Started Locale Service.
Jun 24 08:48:52 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.freedesktop.impl.portal.PermissionStore' requested by ':1.3' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:52 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 24 08:48:52 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.UPower' unit='upower.service' requested by ':1.41' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:52 galelhiani systemd[1]: Starting Daemon for power management...
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.GeoClue2' unit='geoclue.service' requested by ':1.41' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:53 galelhiani systemd[1]: Starting Location Lookup Service...
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.UPower'
Jun 24 08:48:53 galelhiani systemd[1]: Started Daemon for power management.
Jun 24 08:48:53 galelhiani polkitd(authority=local)[854]: Registered Authentication Agent for unix-session:c1 (system bus name :1.41 [/usr/bin/gnome-shell], object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.PackageKit' unit='packagekit.service' requested by ':1.41' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:53 galelhiani systemd[1]: Starting PackageKit Daemon...
Jun 24 08:48:53 galelhiani gnome-shell[1184]: Extension ubuntu-appindicators@ubuntu.com already installed in /usr/share/gnome-shell/extensions/ubuntu-appindicators@ubuntu.com. /usr/share/gnome-shell/extensions/ubuntu-appindicators@ubuntu.com will not be loaded
Jun 24 08:48:53 galelhiani gnome-shell[1184]: Extension ding@rastersoft.com already installed in /usr/share/gnome-shell/extensions/ding@rastersoft.com. /usr/share/gnome-shell/extensions/ding@rastersoft.com will not be loaded
Jun 24 08:48:53 galelhiani gnome-shell[1184]: Extension ubuntu-dock@ubuntu.com already installed in /usr/share/gnome-shell/extensions/ubuntu-dock@ubuntu.com. /usr/share/gnome-shell/extensions/ubuntu-dock@ubuntu.com will not be loaded
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.gnome.Shell.Notifications' requested by ':1.3' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1215]: dbus-daemon[1215]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:53 galelhiani PackageKit[1236]: daemon start
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1215]: dbus-daemon[1215]: Successfully activated service 'org.a11y.atspi.Registry'
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1241]: SpiRegistry daemon is running with well-known name - org.a11y.atspi.Registry
Jun 24 08:48:53 galelhiani org.gnome.Shell.desktop[1184]: Window manager warning: Failed to parse saved session file: Failed to open file “/var/lib/gdm3/.config/mutter/sessions/10eb93f3e4407dc454178229093246765200000011760000.ms”: No such file or directory
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.GeoClue2'
Jun 24 08:48:53 galelhiani systemd[1]: Started Location Lookup Service.
Jun 24 08:48:53 galelhiani gnome-shell[1184]: JS ERROR: TypeError: this._managerProxy is undefined
                                              _onGeoclueVanished@resource:///org/gnome/shell/ui/status/location.js:169:9
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.gnome.Shell.Notifications'
Jun 24 08:48:53 galelhiani gnome-shell[1184]: Error looking up permission: GDBus.Error:org.freedesktop.portal.Error.NotFound: No entry for geolocation
Jun 24 08:48:53 galelhiani org.gnome.Shell.desktop[1223]: Failed to initialize glamor, falling back to sw
Jun 24 08:48:53 galelhiani NetworkManager[845]: <info>  [1782290933.0536] agent-manager: agent[e4e8ec5549caafa3,:1.41/org.gnome.Shell.NetworkAgent/131]: agent registered
Jun 24 08:48:53 galelhiani kernel: rfkill: input handler disabled
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.PackageKit'
Jun 24 08:48:53 galelhiani systemd[1]: Started PackageKit Daemon.
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.gtk.vfs.Daemon' requested by ':1.21' (uid=131 pid=1265 comm="ibus-daemon --panel disable " label="unconfined")
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.freedesktop.systemd1' requested by ':1.22' (uid=131 pid=1254 comm="/usr/libexec/gsd-sharing " label="unconfined")
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activated service 'org.freedesktop.systemd1' failed: Process org.freedesktop.systemd1 exited with status 1
Jun 24 08:48:53 galelhiani gsd-sharing[1254]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
Jun 24 08:48:53 galelhiani gsd-sharing[1254]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.freedesktop.portal.IBus' requested by ':1.21' (uid=131 pid=1265 comm="ibus-daemon --panel disable " label="unconfined")
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.41' (uid=131 pid=1184 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:53 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 08:48:53 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 08:48:53 galelhiani gnome-shell[1184]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.ColorManager' unit='colord.service' requested by ':1.54' (uid=131 pid=1261 comm="/usr/libexec/gsd-color " label="unconfined")
Jun 24 08:48:53 galelhiani systemd[1]: Starting Manage, Install and Generate Color Profiles...
Jun 24 08:48:53 galelhiani colord[1386]: failed to get edid data: EDID length is too small
Jun 24 08:48:53 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.ColorManager'
Jun 24 08:48:53 galelhiani systemd[1]: Started Manage, Install and Generate Color Profiles.
Jun 24 08:48:53 galelhiani gsd-media-keys[1268]: Failed to grab accelerator for keybinding settings:hibernate
Jun 24 08:48:53 galelhiani gsd-media-keys[1268]: Failed to grab accelerator for keybinding settings:playback-repeat
Jun 24 08:48:53 galelhiani gsd-color[1261]: failed to get edid: unable to get EDID for output
Jun 24 08:48:53 galelhiani gnome-shell[1184]: ATK Bridge is disabled but a11y has already been enabled.
Jun 24 08:48:53 galelhiani gsd-color[1261]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 08:48:53 galelhiani spice-vdagent[1397]: vdagent started
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.gnome.ScreenSaver' requested by ':1.26' (uid=131 pid=1274 comm="/usr/libexec/gsd-power " label="unconfined")
Jun 24 08:48:53 galelhiani org.gnome.Shell.desktop[1402]: The XKEYBOARD keymap compiler (xkbcomp) reports:
Jun 24 08:48:53 galelhiani org.gnome.Shell.desktop[1402]: > Warning:          Unsupported maximum keycode 708, clipping.
Jun 24 08:48:53 galelhiani org.gnome.Shell.desktop[1402]: >                   X11 cannot support keycodes above 255.
Jun 24 08:48:53 galelhiani org.gnome.Shell.desktop[1402]: Errors from xkbcomp are not fatal to the X server
Jun 24 08:48:53 galelhiani gnome-shell[1184]: Registering session with GDM
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Activating service name='org.freedesktop.portal.IBus' requested by ':1.35' (uid=131 pid=1398 comm="ibus-daemon --panel disable -r --xim " label="unconfined")
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 24 08:48:53 galelhiani systemd[1]: Starting Agent daemon for Spice guests...
Jun 24 08:48:53 galelhiani systemd[1]: Started Agent daemon for Spice guests.
Jun 24 08:48:53 galelhiani /usr/libexec/gdm-wayland-session[1175]: dbus-daemon[1175]: [session uid=131 pid=1175] Successfully activated service 'org.gnome.ScreenSaver'
Jun 24 08:48:53 galelhiani spice-vdagent[1397]: No SPICE display found for connector Virtual-1
Jun 24 08:48:53 galelhiani spice-vdagent[1397]: vdagent_mutter_get_resolutions: No Spice display ID matching - assuming display ID == Monitor index
Jun 24 08:48:53 galelhiani spice-vdagent[1397]: warning could not get file xfer save dir, file transfers will be disabled
Jun 24 08:48:53 galelhiani spice-vdagent[1397]: File transfer is disabled
Jun 24 08:48:53 galelhiani spice-vdagentd[1429]: opening vdagent virtio channel
Jun 24 08:48:53 galelhiani gnome-session-binary[1176]: Entering running state
Jun 24 08:48:53 galelhiani kernel: input: spice vdagent tablet as /devices/virtual/input/input3
Jun 24 08:48:53 galelhiani xbrlapi.desktop[1440]: openConnection: connect: No such file or directory
Jun 24 08:48:53 galelhiani xbrlapi.desktop[1440]: cannot connect to braille devices daemon brltty at :0
Jun 24 08:48:56 galelhiani gdm-password][1450]: gkr-pam: unable to locate daemon control file
Jun 24 08:48:56 galelhiani gdm-password][1450]: gkr-pam: stashed password to try later in open session
Jun 24 08:48:56 galelhiani gdm-password][1450]: pam_unix(gdm-password:session): session opened for user galelhiani(uid=1000) by (uid=0)
Jun 24 08:48:56 galelhiani systemd[1]: Created slice User Slice of UID 1000.
Jun 24 08:48:56 galelhiani systemd[1]: Starting User Runtime Directory /run/user/1000...
Jun 24 08:48:56 galelhiani systemd-logind[883]: New session 2 of user galelhiani.
Jun 24 08:48:56 galelhiani systemd[1]: Finished User Runtime Directory /run/user/1000.
Jun 24 08:48:56 galelhiani systemd[1]: Starting User Manager for UID 1000...
Jun 24 08:48:56 galelhiani systemd[1458]: pam_unix(systemd-user:session): session opened for user galelhiani(uid=1000) by (uid=0)
Jun 24 08:48:56 galelhiani systemd[1458]: Queued start job for default target Main User Target.
Jun 24 08:48:56 galelhiani systemd[1458]: Created slice User Application Slice.
Jun 24 08:48:56 galelhiani rtkit-daemon[1169]: Supervising 6 threads of 3 processes of 1 users.
Jun 24 08:48:56 galelhiani systemd[1458]: Created slice User Core Session Slice.
Jun 24 08:48:56 galelhiani gdm-password][1450]: gkr-pam: gnome-keyring-daemon started properly and unlocked keyring
Jun 24 08:48:56 galelhiani systemd[1458]: Started Pending report trigger for Ubuntu Report.
Jun 24 08:48:56 galelhiani systemd[1458]: Reached target Paths.
Jun 24 08:48:56 galelhiani systemd[1458]: Reached target Timers.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1465 of process 1465 owned by '1000' high priority at nice level -11.
Jun 24 08:48:56 galelhiani systemd[1458]: Starting D-Bus User Message Bus Socket...
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 7 threads of 4 processes of 2 users.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on GnuPG network certificate management daemon.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 7 threads of 4 processes of 2 users.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on GnuPG cryptographic agent and passphrase cache.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on PipeWire Multimedia System Socket.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on debconf communication socket.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on Sound System.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on REST API socket for snapd user session agent.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on Speech Dispatcher Socket.
Jun 24 08:48:56 galelhiani systemd[1458]: Listening on D-Bus User Message Bus Socket.
Jun 24 08:48:56 galelhiani systemd[1458]: Reached target Sockets.
Jun 24 08:48:56 galelhiani systemd[1458]: Reached target Basic System.
Jun 24 08:48:56 galelhiani systemd[1]: Started User Manager for UID 1000.
Jun 24 08:48:56 galelhiani systemd[1458]: Started PipeWire Multimedia Service.
Jun 24 08:48:56 galelhiani systemd[1458]: Started PipeWire Media Session Manager.
Jun 24 08:48:56 galelhiani systemd[1]: Started Session 2 of User galelhiani.
Jun 24 08:48:56 galelhiani systemd[1458]: Starting Sound Service...
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1467 of process 1467 owned by '1000' high priority at nice level -11.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 8 threads of 5 processes of 2 users.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 8 threads of 5 processes of 2 users.
Jun 24 08:48:57 galelhiani systemd[1458]: Started D-Bus User Message Bus.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] AppArmor D-Bus mediation is enabled
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1468 of process 1466 owned by '1000' RT at priority 20.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 9 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 9 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1475 of process 1465 owned by '1000' RT at priority 20.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 10 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani kernel: rfkill: input handler enabled
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 10 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1489 of process 1467 owned by '1000' RT at priority 5.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 11 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani systemd[1458]: Started Sound Service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target Main User Target.
Jun 24 08:48:57 galelhiani systemd[1458]: Startup finished in 141ms.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 11 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani spice-vdagentd[1429]: closed vdagent virtio channel
Jun 24 08:48:57 galelhiani systemd[1458]: Created slice Slice /app/gnome-session-manager.
Jun 24 08:48:57 galelhiani systemd[1458]: Created slice User Background Tasks Slice.
Jun 24 08:48:57 galelhiani systemd[1458]: Started Path trigger for Apport crash notifications.
Jun 24 08:48:57 galelhiani systemd[1458]: Started Path trigger for new release of Ubuntu notifications.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Wayland Session.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Shell.
Jun 24 08:48:57 galelhiani systemd[1458]: Condition check resulted in GNOME Initial Setup Copy Worker being skipped.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Start gnome-keyring as SSH agent...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Start gnome-keyring for the Secrets Service, and PKCS #11...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Monitor Session leader for GNOME Session...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Session Migration...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Rewrite dynamic launcher portal entries...
Jun 24 08:48:57 galelhiani systemd[1458]: Finished Session Migration.
Jun 24 08:48:57 galelhiani systemd[1458]: Started Monitor Session leader for GNOME Session.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.Daemon' unit='gvfs-daemon.service' requested by ':1.10' (uid=1000 pid=1529 comm="/usr/libexec/xdg-desktop-portal-rewrite-launchers " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem service...
Jun 24 08:48:57 galelhiani systemd[1458]: Finished Start gnome-keyring for the Secrets Service, and PKCS #11.
Jun 24 08:48:57 galelhiani sh[1537]: dbus-update-activation-environment: setting SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 24 08:48:57 galelhiani sh[1537]: dbus-update-activation-environment: setting SSH_AGENT_LAUNCHER=gnome-keyring
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem service.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.Daemon'
Jun 24 08:48:57 galelhiani sh[1522]: /bin/sh: 1: initctl: not found
Jun 24 08:48:57 galelhiani systemd[1458]: Finished Start gnome-keyring as SSH agent.
Jun 24 08:48:57 galelhiani systemd[1458]: Started OpenSSH Agent.
Jun 24 08:48:57 galelhiani systemd[1458]: Finished Rewrite dynamic launcher portal entries.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target Session services which should run early before the graphical session is brought up.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target Tasks to be run before GNOME Session starts.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME Session Manager (session: ubuntu)...
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1521 of process 1467 owned by '1000' RT at priority 5.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 12 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani pulseaudio[1467]: ALSA woke us up to read new data from the device, but there was actually nothing to read.
Jun 24 08:48:57 galelhiani pulseaudio[1467]: Most likely this is a bug in the ALSA driver 'virtio_snd'. Please report this issue to the ALSA developers.
Jun 24 08:48:57 galelhiani pulseaudio[1467]: We were woken up with POLLIN set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 24 08:48:57 galelhiani gnome-keyring-secrets.desktop[1560]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 24 08:48:57 galelhiani gnome-keyring-daemon[1471]: The Secret Service was already initialized
Jun 24 08:48:57 galelhiani gnome-keyring-daemon[1471]: The PKCS#11 component was already initialized
Jun 24 08:48:57 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:57 galelhiani gnome-keyring-pkcs11.desktop[1562]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 12 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME Session Manager (session: ubuntu).
Jun 24 08:48:57 galelhiani gnome-keyring-daemon[1471]: The SSH agent was already initialized
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Session Manager is ready.
Jun 24 08:48:57 galelhiani gnome-keyring-ssh.desktop[1563]: SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME Shell on Wayland...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME Shell on X11...
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 24 08:48:57 galelhiani systemd[1458]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 1.
Jun 24 08:48:57 galelhiani systemd[1458]: Stopped GNOME Shell on X11.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME Shell on X11...
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 24 08:48:57 galelhiani systemd[1458]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 2.
Jun 24 08:48:57 galelhiani systemd[1458]: Stopped GNOME Shell on X11.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME Shell on X11...
Jun 24 08:48:57 galelhiani gnome-session[1543]: gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1557: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1557 does not exist.
Jun 24 08:48:57 galelhiani gnome-session[1543]: gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1559: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1559 does not exist.
Jun 24 08:48:57 galelhiani gnome-session[1543]: gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1568: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1568 does not exist.
Jun 24 08:48:57 galelhiani gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1557: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1557 does not exist.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 24 08:48:57 galelhiani gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1559: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1559 does not exist.
Jun 24 08:48:57 galelhiani systemd[1458]: Condition check resulted in GNOME Shell on X11 being skipped.
Jun 24 08:48:57 galelhiani gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1568: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1568 does not exist.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Scheduled restart job, restart counter is at 3.
Jun 24 08:48:57 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:57 galelhiani systemd[1458]: Stopped GNOME Shell on X11.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Start request repeated too quickly.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.Shell@x11.service: Skipped due to 'exec-condition'.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME Shell on X11.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Successfully made thread 1561 of process 1467 owned by '1000' RT at priority 5.
Jun 24 08:48:57 galelhiani rtkit-daemon[1169]: Supervising 13 threads of 6 processes of 2 users.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Running GNOME Shell (using mutter 42.9) as a Wayland display server
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Added device '/dev/dri/card0' (virtio_gpu) using non-atomic mode setting.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Enabling experimental feature 'scale-monitor-framebuffer'
Jun 24 08:48:57 galelhiani pulseaudio[1467]: ALSA woke us up to write new data to the device, but there was actually nothing to write.
Jun 24 08:48:57 galelhiani pulseaudio[1467]: Most likely this is a bug in the ALSA driver 'virtio_snd'. Please report this issue to the ALSA developers.
Jun 24 08:48:57 galelhiani pulseaudio[1467]: We were woken up with POLLOUT set -- however a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Failed to initialize accelerated iGPU/dGPU framebuffer sharing: Not hardware accelerated
Jun 24 08:48:57 galelhiani gnome-shell[1566]: libEGL warning: egl: failed to create dri2 screen
Jun 24 08:48:57 galelhiani gnome-shell[1566]: libEGL warning: NEEDS EXTENSION: falling back to kms_swrast
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Created gbm renderer for '/dev/dri/card0'
Jun 24 08:48:57 galelhiani gnome-shell[1566]: GPU /dev/dri/card0 selected as primary
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Failed to use stored monitor configuration: Invalid mode 3024x1898 (60.003105) for monitor 'unknown unknown'
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Disabling DMA buffer screen sharing (not hardware accelerated)
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Using public X11 display :0, (using :1 for managed services)
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Using Wayland display name 'wayland-0'
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Unset XDG_SESSION_ID, getCurrentSessionProxy() called outside a user session. Asking logind directly.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Will monitor session 2
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.freedesktop.impl.portal.PermissionStore' unit='xdg-permission-store.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.Shell.CalendarServer' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting sandboxed app permission store...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.impl.portal.PermissionStore'
Jun 24 08:48:57 galelhiani systemd[1458]: Started sandboxed app permission store.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gnome.evolution.dataserver.Sources5' unit='evolution-source-registry.service' requested by ':1.29' (uid=1000 pid=1606 comm="/usr/libexec/gnome-shell-calendar-server " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Evolution source registry...
Jun 24 08:48:57 galelhiani polkitd(authority=local)[854]: Registered Authentication Agent for unix-session:2 (system bus name :1.78 [/usr/bin/gnome-shell], object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Telepathy is not available, chat integration will be disabled.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem service - disk device monitor...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.OnlineAccounts' requested by ':1.30' (uid=1000 pid=1615 comm="/usr/libexec/evolution-source-registry " label="unconfined")
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.UDisks2VolumeMonitor'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem service - disk device monitor.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.evolution.dataserver.Sources5'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Evolution source registry.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.GoaVolumeMonitor' unit='gvfs-goa-volume-monitor.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem service - GNOME Online Accounts monitor...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gnome.evolution.dataserver.Calendar8' unit='evolution-calendar-factory.service' requested by ':1.29' (uid=1000 pid=1606 comm="/usr/libexec/gnome-shell-calendar-server " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Evolution calendar service...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.Shell.CalendarServer'
Jun 24 08:48:57 galelhiani goa-daemon[1622]: goa-daemon version 3.44.0 starting
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.Identity' requested by ':1.34' (uid=1000 pid=1622 comm="/usr/libexec/goa-daemon " label="unconfined")
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.OnlineAccounts'
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.GoaVolumeMonitor'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem service - GNOME Online Accounts monitor.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.GPhoto2VolumeMonitor' unit='gvfs-gphoto2-volume-monitor.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem service - digital camera monitor...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.evolution.dataserver.Calendar8'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Evolution calendar service.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.Identity'
Jun 24 08:48:57 galelhiani evolution-calen[1632]: e_source_unset_last_credentials_required_arguments: assertion 'E_IS_SOURCE (source)' failed
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='ca.desrt.dconf' unit='dconf.service' requested by ':1.33' (uid=1000 pid=1632 comm="/usr/libexec/evolution-calendar-factory " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting User preferences database...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gnome.evolution.dataserver.AddressBook10' unit='evolution-addressbook-factory.service' requested by ':1.33' (uid=1000 pid=1632 comm="/usr/libexec/evolution-calendar-factory " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Evolution address book service...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.GPhoto2VolumeMonitor'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem service - digital camera monitor.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'ca.desrt.dconf'
Jun 24 08:48:57 galelhiani systemd[1458]: Started User preferences database.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.MTPVolumeMonitor' unit='gvfs-mtp-volume-monitor.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem service - Media Transfer Protocol monitor...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.MTPVolumeMonitor'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem service - Media Transfer Protocol monitor.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.AfcVolumeMonitor' unit='gvfs-afc-volume-monitor.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem service - Apple File Conduit monitor...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem service - Apple File Conduit monitor.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.evolution.dataserver.AddressBook10'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Evolution address book service.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Failed to import DBusMenu, quicklists are not avaialble: Error: Requiring Dbusmenu, version none: Typelib file for namespace 'Dbusmenu' (any version) not found
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.freedesktop.FileManager1' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.Shell.Notifications' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani at-spi-dbus-bus.desktop[1576]: dbus-daemon[1576]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani at-spi-dbus-bus.desktop[1576]: dbus-daemon[1576]: Successfully activated service 'org.a11y.atspi.Registry'
Jun 24 08:48:57 galelhiani at-spi-dbus-bus.desktop[1698]: SpiRegistry daemon is running with well-known name - org.a11y.atspi.Registry
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME Shell on Wayland.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Session is initialized.
Jun 24 08:48:57 galelhiani systemd[1458]: GNOME session X11 services is inactive.
Jun 24 08:48:57 galelhiani systemd[1458]: Dependency failed for GNOME XSettings service.
Jun 24 08:48:57 galelhiani systemd[1458]: org.gnome.SettingsDaemon.XSettings.service: Job org.gnome.SettingsDaemon.XSettings.service/start failed with result 'dependency'.
Jun 24 08:48:57 galelhiani systemd[1458]: gnome-session-x11-services-ready.target: Job gnome-session-x11-services-ready.target/verify-active failed with result 'dependency'.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Session (session: ubuntu).
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME XSettings target.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Signal initialization done to GNOME Session Manager...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting IBus Daemon for GNOME...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME accessibility service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME color management service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME date & time service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME maintenance of expirable data service...
Jun 24 08:48:57 galelhiani kernel: ISO 9660 Extensions: Microsoft Joliet Level 3
Jun 24 08:48:57 galelhiani udisksd[884]: Mounted /dev/sda1 at /media/galelhiani/Ubuntu-Server 22.04.5 LTS arm64 on behalf of uid 1000
Jun 24 08:48:57 galelhiani kernel: ISO 9660 Extensions: RRIP_1991A
Jun 24 08:48:57 galelhiani spice-vdagent[1735]: vdagent started
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME keyboard configuration service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME keyboard shortcuts service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME power management service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME printer notifications service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME RFKill support service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME FreeDesktop screensaver service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME file sharing service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME smartcard service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME sound sample caching service...
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME Wacom tablet support service...
Jun 24 08:48:57 galelhiani systemd[1458]: Finished Signal initialization done to GNOME Session Manager.
Jun 24 08:48:57 galelhiani gnome-shell[1753]: (WW) Option "-listen" for file descriptors is deprecated
Jun 24 08:48:57 galelhiani gnome-shell[1753]: Please use "-listenfd" instead.
Jun 24 08:48:57 galelhiani gnome-shell[1753]: (WW) Option "-listen" for file descriptors is deprecated
Jun 24 08:48:57 galelhiani gnome-shell[1753]: Please use "-listenfd" instead.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME accessibility service.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME maintenance of expirable data service.
Jun 24 08:48:57 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME accessibility target.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME maintenance of expirable data target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME date & time service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME date & time target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME smartcard service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME smartcard target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME file sharing service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME file sharing target.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.Shell.Notifications'
Jun 24 08:48:57 galelhiani NetworkManager[845]: <info>  [1782290937.6340] agent-manager: agent[6b1dfba3b0e1aa84,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME sound sample caching service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME sound sample caching target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME RFKill support service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME RFKill support target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME FreeDesktop screensaver service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME FreeDesktop screensaver target.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Error looking up permission: GDBus.Error:org.freedesktop.portal.Error.NotFound: No entry for geolocation
Jun 24 08:48:57 galelhiani kernel: rfkill: input handler disabled
Jun 24 08:48:57 galelhiani gnome-shell[1753]: libEGL warning: egl: failed to create dri2 screen
Jun 24 08:48:57 galelhiani gnome-shell[1753]: libEGL warning: NEEDS EXTENSION: falling back to kms_swrast
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.freedesktop.portal.IBus' requested by ':1.61' (uid=1000 pid=1796 comm="/usr/bin/ibus-daemon --panel disable " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Started IBus Daemon for GNOME.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.portal.IBus'
Jun 24 08:48:57 galelhiani gnome-shell[1753]: Failed to initialize glamor, falling back to sw
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME session X11 services.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting GNOME XSettings service...
Jun 24 08:48:57 galelhiani gnome-shell[1834]: The XKEYBOARD keymap compiler (xkbcomp) reports:
Jun 24 08:48:57 galelhiani gnome-shell[1834]: > Warning:          Unsupported maximum keycode 708, clipping.
Jun 24 08:48:57 galelhiani gnome-shell[1834]: >                   X11 cannot support keycodes above 255.
Jun 24 08:48:57 galelhiani gnome-shell[1834]: Errors from xkbcomp are not fatal to the X server
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gtk.vfs.Metadata' unit='gvfs-metadata.service' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.Shell.HotplugSniffer' requested by ':1.26' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Virtual filesystem metadata service...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.Shell.HotplugSniffer'
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME keyboard configuration service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME keyboard configuration target.
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 08:48:57 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.freedesktop.portal.Desktop' unit='xdg-desktop-portal.service' requested by ':1.43' (uid=1000 pid=1684 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Portal service...
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME Wacom tablet support service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Wacom tablet support target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME printer notifications service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME printer notifications target.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gtk.vfs.Metadata'
Jun 24 08:48:57 galelhiani systemd[1458]: Started Virtual filesystem metadata service.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.freedesktop.portal.Documents' unit='xdg-document-portal.service' requested by ':1.76' (uid=1000 pid=1844 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting flatpak document portal service...
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME keyboard shortcuts service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME keyboard shortcuts target.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.portal.Documents'
Jun 24 08:48:57 galelhiani systemd[1458]: Started flatpak document portal service.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME color management service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME color management target.
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME power management service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME power management target.
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.freedesktop.impl.portal.desktop.gnome' unit='xdg-desktop-portal-gnome.service' requested by ':1.76' (uid=1000 pid=1844 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Portal service (GNOME implementation)...
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ScreenSaver' requested by ':1.59' (uid=1000 pid=1737 comm="/usr/libexec/gsd-power " label="unconfined")
Jun 24 08:48:57 galelhiani gsd-media-keys[1734]: Failed to grab accelerator for keybinding settings:hibernate
Jun 24 08:48:57 galelhiani gsd-media-keys[1734]: Failed to grab accelerator for keybinding settings:playback-repeat
Jun 24 08:48:57 galelhiani gsd-color[1720]: failed to get edid: unable to get EDID for output
Jun 24 08:48:57 galelhiani gsd-color[1261]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 08:48:57 galelhiani gsd-color[1720]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 08:48:57 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ScreenSaver'
Jun 24 08:48:57 galelhiani systemd[1458]: Started GNOME XSettings service.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME session X11 services.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Session.
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target GNOME Wayland Session (session: ubuntu).
Jun 24 08:48:57 galelhiani systemd[1458]: Reached target Current graphical user session.
Jun 24 08:48:57 galelhiani systemd[1458]: Condition check resulted in GNOME Initial Setup being skipped.
Jun 24 08:48:57 galelhiani systemd[1458]: Starting Tracker file system data miner...
Jun 24 08:48:57 galelhiani gnome-shell[1566]: ATK Bridge is disabled but a11y has already been enabled.
Jun 24 08:48:58 galelhiani spice-vdagent[1735]: No SPICE display found for connector Virtual-1
Jun 24 08:48:58 galelhiani spice-vdagent[1735]: vdagent_mutter_get_resolutions: No Spice display ID matching - assuming display ID == Monitor index
Jun 24 08:48:58 galelhiani gnome-shell[1566]: GNOME Shell started at Wed Jun 24 2026 08:48:57 GMT+0000 (UTC)
Jun 24 08:48:58 galelhiani gnome-shell[1566]: Registering session with GDM
Jun 24 08:48:58 galelhiani spice-vdagentd[1429]: opening vdagent virtio channel
Jun 24 08:48:58 galelhiani kernel: input: spice vdagent tablet as /devices/virtual/input/input4
Jun 24 08:48:58 galelhiani gsd-screensaver[1269]: Error releasing name org.freedesktop.ScreenSaver: The connection is closed
Jun 24 08:48:58 galelhiani gnome-session[1176]: gnome-session-binary[1176]: WARNING: Lost name on bus: org.gnome.SessionManager
Jun 24 08:48:58 galelhiani gnome-session-binary[1176]: WARNING: Lost name on bus: org.gnome.SessionManager
Jun 24 08:48:58 galelhiani gsd-smartcard[1266]: Error releasing name org.gnome.SettingsDaemon.Smartcard: The connection is closed
Jun 24 08:48:58 galelhiani gnome-shell[1184]: Lost or failed to acquire name org.gnome.Mutter.ScreenCast
Jun 24 08:48:58 galelhiani gnome-shell[1184]: Lost or failed to acquire name org.gnome.Mutter.RemoteDesktop
Jun 24 08:48:58 galelhiani gnome-shell[1184]: Connection to xwayland lost
Jun 24 08:48:58 galelhiani gdm-launch-environment][1151]: pam_unix(gdm-launch-environment:session): session closed for user gdm
Jun 24 08:48:58 galelhiani gdm-launch-environment][1151]: GLib-GObject: g_object_unref: assertion 'G_IS_OBJECT (object)' failed
Jun 24 08:48:58 galelhiani systemd-logind[883]: Session c1 logged out. Waiting for processes to exit.
Jun 24 08:48:58 galelhiani gnome-session-binary[1543]: Entering running state
Jun 24 08:48:58 galelhiani at-spi2-registr[1698]: Failed to register client: GDBus.Error:org.gnome.SessionManager.AlreadyRegistered: Unable to register client
Jun 24 08:48:58 galelhiani at-spi2-registr[1698]: Unable to register client with session manager
Jun 24 08:48:58 galelhiani gnome-session[1543]: gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1956: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1956 does not exist.
Jun 24 08:48:58 galelhiani gnome-session-binary[1543]: GnomeDesktop-WARNING: Could not create transient scope for PID 1956: GDBus.Error:org.freedesktop.DBus.Error.UnixProcessIdUnknown: Process with ID 1956 does not exist.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1458]: app-gnome-user\x2ddirs\x2dupdate\x2dgtk-1944.scope: Couldn't move process 1944 to requested cgroup '/user.slice/user-1000.slice/user@1000.service/app.slice/app-gnome-user\x2ddirs\x2dupdate\x2dgtk-1944.scope': No such process
Jun 24 08:48:58 galelhiani systemd[1458]: app-gnome-user\x2ddirs\x2dupdate\x2dgtk-1944.scope: Failed to add PIDs to scope's control group: No such process
Jun 24 08:48:58 galelhiani systemd[1458]: app-gnome-user\x2ddirs\x2dupdate\x2dgtk-1944.scope: Failed with result 'resources'.
Jun 24 08:48:58 galelhiani systemd[1458]: Failed to start Application launched by gnome-session-binary.
Jun 24 08:48:58 galelhiani systemd[1]: session-c1.scope: Deactivated successfully.
Jun 24 08:48:58 galelhiani systemd[1]: session-c1.scope: Consumed 2.093s CPU time.
Jun 24 08:48:58 galelhiani systemd-logind[883]: Removed session c1.
Jun 24 08:48:58 galelhiani parcellite[1942]: Failed to load module "canberra-gtk-module"
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 08:48:58 galelhiani polkitd(authority=local)[854]: Unregistered Authentication Agent for unix-session:c1 (system bus name :1.41, object path /org/freedesktop/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8) (disconnected from bus)
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Flag 0x0001, status 256, EXIT 1 STAT 1
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 08:48:58 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.impl.portal.desktop.gnome'
Jun 24 08:48:58 galelhiani systemd[1458]: Started Portal service (GNOME implementation).
Jun 24 08:48:58 galelhiani gdm3[1033]: Gdm: Child process -1166 was already dead.
Jun 24 08:48:58 galelhiani systemd[1458]: Started Tracker file system data miner.
Jun 24 08:48:58 galelhiani rtkit-daemon[1169]: Supervising 9 threads of 5 processes of 2 users.
Jun 24 08:48:58 galelhiani rtkit-daemon[1169]: Supervising 9 threads of 5 processes of 2 users.
Jun 24 08:48:58 galelhiani rtkit-daemon[1169]: Supervising 9 threads of 5 processes of 2 users.
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.freedesktop.impl.portal.desktop.gtk' unit='xdg-desktop-portal-gtk.service' requested by ':1.76' (uid=1000 pid=1844 comm="/usr/libexec/xdg-desktop-portal " label="unconfined")
Jun 24 08:48:58 galelhiani systemd[1458]: Starting Portal service (GTK/GNOME implementation)...
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.impl.portal.desktop.gtk'
Jun 24 08:48:58 galelhiani systemd[1458]: Started Portal service (GTK/GNOME implementation).
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.portal.Desktop'
Jun 24 08:48:58 galelhiani systemd[1458]: Started Portal service.
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.FileManager1'
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.freedesktop.Tracker3.Miner.Extract' unit='tracker-extract-3.service' requested by ':1.88' (uid=1000 pid=1925 comm="/usr/libexec/tracker-miner-fs-3 " label="unconfined")
Jun 24 08:48:58 galelhiani systemd[1458]: Starting Tracker metadata extractor...
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.93' (uid=1000 pid=1995 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.freedesktop.Tracker3.Miner.Extract'
Jun 24 08:48:58 galelhiani systemd[1458]: Started Tracker metadata extractor.
Jun 24 08:48:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 08:48:58 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 08:48:58 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 08:49:01 galelhiani spice-vdagent[1735]: No SPICE display found for connector Virtual-1
Jun 24 08:49:01 galelhiani spice-vdagent[1735]: vdagent_mutter_get_resolutions: No Spice display ID matching - assuming display ID == Monitor index
Jun 24 08:49:01 galelhiani spice-vdagent[1735]: No SPICE display found for connector Virtual-1
Jun 24 08:49:01 galelhiani spice-vdagent[1735]: vdagent_mutter_get_resolutions: No Spice display ID matching - assuming display ID == Monitor index
Jun 24 08:49:01 galelhiani gsd-color[1720]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 08:49:01 galelhiani gsd-color[1720]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 08:49:01 galelhiani kernel: input: spice vdagent tablet as /devices/virtual/input/input5
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 08:49:01 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 08:49:03 galelhiani nautilus[1684]: Called "net usershare info" but it failed: 'net usershare' returned error 255: net usershare: cannot open usershare directory /var/lib/samba/usershares. Error Permission denied
                                           You do not have permission to create a usershare. Ask your administrator to grant you permissions to create a share.
Jun 24 08:49:08 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gnome.Terminal' unit='gnome-terminal-server.service' requested by ':1.43' (uid=1000 pid=1684 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 08:49:08 galelhiani systemd[1458]: Created slice Slice /app/org.gnome.Terminal.
Jun 24 08:49:08 galelhiani systemd[1458]: Starting GNOME Terminal Server...
Jun 24 08:49:08 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.Terminal'
Jun 24 08:49:08 galelhiani systemd[1458]: Started GNOME Terminal Server.
Jun 24 08:49:08 galelhiani systemd[1458]: Started VTE child process 2116 launched by gnome-terminal-server process 2098.
Jun 24 08:49:08 galelhiani systemd[1]: Stopping User Manager for UID 131...
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped target Main User Target.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopping D-Bus User Message Bus...
Jun 24 08:49:08 galelhiani systemd[1156]: Stopping PipeWire Media Session Manager...
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped D-Bus User Message Bus.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped PipeWire Media Session Manager.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopping PipeWire Multimedia Service...
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped PipeWire Multimedia Service.
Jun 24 08:49:08 galelhiani systemd[1156]: Removed slice User Core Session Slice.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped target Basic System.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped target Paths.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped Pending report trigger for Ubuntu Report.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped target Sockets.
Jun 24 08:49:08 galelhiani systemd[1156]: Stopped target Timers.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed D-Bus User Message Bus Socket.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed GnuPG network certificate management daemon.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed GnuPG cryptographic agent and passphrase cache (access for web browsers).
Jun 24 08:49:08 galelhiani systemd[1156]: Closed GnuPG cryptographic agent and passphrase cache (restricted).
Jun 24 08:49:08 galelhiani systemd[1156]: Closed GnuPG cryptographic agent (ssh-agent emulation).
Jun 24 08:49:08 galelhiani systemd[1156]: Closed GnuPG cryptographic agent and passphrase cache.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed PipeWire Multimedia System Socket.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed debconf communication socket.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed Sound System.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed REST API socket for snapd user session agent.
Jun 24 08:49:08 galelhiani systemd[1156]: Closed Speech Dispatcher Socket.
Jun 24 08:49:08 galelhiani systemd[1156]: Removed slice User Application Slice.
Jun 24 08:49:08 galelhiani systemd[1156]: Reached target Shutdown.
Jun 24 08:49:08 galelhiani systemd[1156]: Finished Exit the Session.
Jun 24 08:49:08 galelhiani systemd[1156]: Reached target Exit the Session.
Jun 24 08:49:08 galelhiani systemd[1]: user@131.service: Deactivated successfully.
Jun 24 08:49:08 galelhiani systemd[1]: Stopped User Manager for UID 131.
Jun 24 08:49:08 galelhiani systemd[1]: Stopping User Runtime Directory /run/user/131...
Jun 24 08:49:08 galelhiani systemd[1]: run-user-131.mount: Deactivated successfully.
Jun 24 08:49:08 galelhiani systemd[1]: user-runtime-dir@131.service: Deactivated successfully.
Jun 24 08:49:08 galelhiani systemd[1]: Stopped User Runtime Directory /run/user/131.
Jun 24 08:49:08 galelhiani systemd[1]: Removed slice User Slice of UID 131.
Jun 24 08:49:08 galelhiani systemd[1]: user-131.slice: Consumed 2.240s CPU time.
Jun 24 08:49:09 galelhiani systemd[1]: systemd-fsckd.service: Deactivated successfully.
Jun 24 08:49:12 galelhiani systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 24 08:49:15 galelhiani systemd-timesyncd[779]: Initial synchronization to time server 185.125.190.58:123 (ntp.ubuntu.com).
Jun 24 08:49:17 galelhiani dbus-daemon[844]: [system] Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
Jun 24 08:49:17 galelhiani pulseaudio[1467]: GetManagedObjects() failed: org.freedesktop.DBus.Error.TimedOut: Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
Jun 24 08:49:21 galelhiani gnome-shell[1566]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 31ms, your system is too slow
Jun 24 08:49:23 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 08:49:27 galelhiani systemd[1]: systemd-localed.service: Deactivated successfully.
Jun 24 08:49:33 galelhiani systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Jun 24 08:49:58 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 08:49:58 galelhiani anacron[2151]: Anacron 2.3 started on 2026-06-24
Jun 24 08:49:58 galelhiani anacron[2151]: Normal exit (0 jobs run)
Jun 24 08:49:58 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 08:49:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:49:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:50:00 galelhiani pkexec[2190]: pam_unix(polkit-1:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 08:50:00 galelhiani pkexec[2190]: galelhiani: Executing command [USER=root] [TTY=unknown] [CWD=/home/galelhiani] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Jun 24 08:50:00 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 08:50:00 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 08:50:58 galelhiani systemd[1458]: Started Application launched by gnome-session-binary.
Jun 24 08:53:41 galelhiani systemd[1]: Starting Download data for packages that failed at package install time...
Jun 24 08:53:41 galelhiani systemd[1]: update-notifier-download.service: Deactivated successfully.
Jun 24 08:53:41 galelhiani systemd[1]: Finished Download data for packages that failed at package install time.
Jun 24 08:53:42 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.28' (uid=0 pid=867 comm="/usr/lib/snapd/snapd " label="unconfined")
Jun 24 08:53:42 galelhiani systemd[1]: Starting Time & Date Service...
Jun 24 08:53:42 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.timedate1'
Jun 24 08:53:42 galelhiani systemd[1]: Started Time & Date Service.
Jun 24 08:54:12 galelhiani systemd[1]: systemd-timedated.service: Deactivated successfully.
Jun 24 08:54:28 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 08:54:28 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 08:57:33 galelhiani systemd-resolved[830]: Clock change detected. Flushing caches.
Jun 24 09:03:44 galelhiani systemd[1]: Starting Cleanup of Temporary Directories...
Jun 24 09:03:44 galelhiani systemd[1]: systemd-tmpfiles-clean.service: Deactivated successfully.
Jun 24 09:03:44 galelhiani systemd[1]: Finished Cleanup of Temporary Directories.
Jun 24 09:17:01 galelhiani CRON[2255]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 09:17:01 galelhiani CRON[2256]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 09:17:01 galelhiani CRON[2255]: pam_unix(cron:session): session closed for user root
Jun 24 09:30:01 galelhiani CRON[2266]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 09:30:01 galelhiani CRON[2267]: (root) CMD ([ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi)
Jun 24 09:30:01 galelhiani CRON[2266]: pam_unix(cron:session): session closed for user root
Jun 24 09:33:19 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 09:33:19 galelhiani anacron[2269]: Anacron 2.3 started on 2026-06-24
Jun 24 09:33:19 galelhiani anacron[2269]: Normal exit (0 jobs run)
Jun 24 09:33:19 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 10:17:01 galelhiani CRON[2306]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 10:17:01 galelhiani CRON[2307]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 10:17:01 galelhiani CRON[2306]: pam_unix(cron:session): session closed for user root
Jun 24 10:21:13 galelhiani systemd[1]: Starting Message of the Day...
Jun 24 10:21:14 galelhiani 50-motd-news[2349]:  * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
Jun 24 10:21:14 galelhiani 50-motd-news[2349]:    just raised the bar for easy, resilient and secure K8s cluster deployment.
Jun 24 10:21:14 galelhiani 50-motd-news[2349]:    https://ubuntu.com/engage/secure-kubernetes-at-the-edge
Jun 24 10:21:14 galelhiani systemd[1]: motd-news.service: Deactivated successfully.
Jun 24 10:21:14 galelhiani systemd[1]: Finished Message of the Day.
Jun 24 10:30:01 galelhiani CRON[2361]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 10:30:01 galelhiani CRON[2362]: (root) CMD ([ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi)
Jun 24 10:30:01 galelhiani CRON[2361]: pam_unix(cron:session): session closed for user root
Jun 24 10:32:19 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 10:32:19 galelhiani anacron[2364]: Anacron 2.3 started on 2026-06-24
Jun 24 10:32:19 galelhiani anacron[2364]: Normal exit (0 jobs run)
Jun 24 10:32:19 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 11:01:24 galelhiani systemd-resolved[830]: Clock change detected. Flushing caches.
Jun 24 11:17:01 galelhiani CRON[2380]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 11:17:01 galelhiani CRON[2381]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 11:17:01 galelhiani CRON[2380]: pam_unix(cron:session): session closed for user root
Jun 24 12:28:20 galelhiani systemd-resolved[830]: Clock change detected. Flushing caches.
Jun 24 12:28:20 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 12:28:20 galelhiani anacron[2396]: Anacron 2.3 started on 2026-06-24
Jun 24 12:28:20 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 12:28:20 galelhiani anacron[2396]: Normal exit (0 jobs run)
Jun 24 12:28:52 galelhiani CRON[2401]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 12:28:52 galelhiani CRON[2402]: (root) CMD ([ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi)
Jun 24 12:28:52 galelhiani CRON[2401]: pam_unix(cron:session): session closed for user root
Jun 24 12:38:02 galelhiani systemd-resolved[830]: Clock change detected. Flushing caches.
Jun 24 12:38:02 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 12:38:02 galelhiani anacron[2403]: Anacron 2.3 started on 2026-06-24
Jun 24 12:38:02 galelhiani anacron[2403]: Normal exit (0 jobs run)
Jun 24 12:38:02 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 12:38:10 galelhiani CRON[2404]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 12:38:10 galelhiani CRON[2405]: (root) CMD ([ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi)
Jun 24 12:38:10 galelhiani CRON[2404]: pam_unix(cron:session): session closed for user root
Jun 24 12:39:04 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 12:39:04 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 12:39:56 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.78' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 12:39:56 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 12:39:56 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 12:39:56 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 12:39:56 galelhiani gnome-shell[1566]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 12:39:58 galelhiani gdm-password][2422]: gkr-pam: unlocked login keyring
Jun 24 12:39:58 galelhiani NetworkManager[845]: <info>  [1782304798.2315] agent-manager: agent[b33e9347c3b9fdc7,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 12:39:58 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 12:39:58 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 12:39:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.111' (uid=1000 pid=2428 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 12:39:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 12:39:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 12:39:58 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 12:39:58 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 12:40:26 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 12:47:46 galelhiani systemd[1458]: Started Application launched by gsd-media-keys.
Jun 24 12:47:46 galelhiani gsd-media-keys[2503]: Converted:
Jun 24 12:48:46 galelhiani galelhiani[2536]: hello
Jun 24 12:50:41 galelhiani gnome-shell[1566]: JS ERROR: TypeError: this.actor is null
                                              _syncEnabled@resource:///org/gnome/shell/ui/windowManager.js:138:25
                                              onStopped@resource:///org/gnome/shell/ui/windowManager.js:150:35
                                              _makeEaseCallback/<@resource:///org/gnome/shell/ui/environment.js:151:22
                                              _easeActorProperty/<@resource:///org/gnome/shell/ui/environment.js:317:60
                                              _destroyWindowDone@resource:///org/gnome/shell/ui/windowManager.js:1596:21
                                              onStopped@resource:///org/gnome/shell/ui/windowManager.js:1564:39
                                              _makeEaseCallback/<@resource:///org/gnome/shell/ui/environment.js:151:22
                                              _easeActor/<@resource:///org/gnome/shell/ui/environment.js:240:64
Jun 24 12:50:41 galelhiani systemd[1458]: gnome-terminal-server.service: Consumed 5.330s CPU time.
Jun 24 12:50:44 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating via systemd: service name='org.gnome.Terminal' unit='gnome-terminal-server.service' requested by ':1.43' (uid=1000 pid=1684 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 12:50:44 galelhiani systemd[1458]: Starting GNOME Terminal Server...
Jun 24 12:50:44 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.Terminal'
Jun 24 12:50:44 galelhiani systemd[1458]: Started GNOME Terminal Server.
Jun 24 12:50:44 galelhiani systemd[1458]: Started VTE child process 2585 launched by gnome-terminal-server process 2567.
Jun 24 12:53:11 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 12:53:11 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 12:57:00 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 12:57:00 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:01:36 galelhiani systemd[1]: Starting Refresh fwupd metadata and update motd...
Jun 24 13:01:36 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='org.freedesktop.fwupd' unit='fwupd.service' requested by ':1.109' (uid=111 pid=2632 comm="/usr/bin/fwupdmgr refresh " label="unconfined")
Jun 24 13:01:36 galelhiani systemd[1]: Starting Firmware update daemon...
Jun 24 13:01:36 galelhiani dbus-daemon[844]: [system] Successfully activated service 'org.freedesktop.fwupd'
Jun 24 13:01:36 galelhiani systemd[1]: Started Firmware update daemon.
Jun 24 13:01:36 galelhiani systemd[1]: fwupd-refresh.service: Deactivated successfully.
Jun 24 13:01:36 galelhiani systemd[1]: Finished Refresh fwupd metadata and update motd.
Jun 24 13:03:05 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.78' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 13:03:05 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 13:03:05 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 13:03:05 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 13:03:05 galelhiani gnome-shell[1566]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 13:03:07 galelhiani gdm-password][2656]: gkr-pam: unlocked login keyring
Jun 24 13:03:07 galelhiani NetworkManager[845]: <info>  [1782306187.5601] agent-manager: agent[7d1bb50a338f404d,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 13:03:07 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 13:03:07 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 13:03:07 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.118' (uid=1000 pid=2661 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 13:03:07 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 13:03:07 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 13:03:07 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 13:03:07 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 13:03:35 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 13:17:01 galelhiani CRON[2830]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 13:17:01 galelhiani CRON[2831]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 13:17:01 galelhiani CRON[2830]: pam_unix(cron:session): session closed for user root
Jun 24 13:23:29 galelhiani gnome-shell[1566]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 24ms, your system is too slow
Jun 24 13:23:36 galelhiani sudo[2889]: galelhiani : TTY=pts/0 ; PWD=/home/galelhiani/Desktop/git/devops/linux_system_storage ; USER=root ; COMMAND=/usr/bin/apt install nmon
Jun 24 13:23:36 galelhiani sudo[2889]: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 13:23:40 galelhiani sudo[2889]: pam_unix(sudo:session): session closed for user root
Jun 24 13:24:33 galelhiani gnome-shell[1566]: Window manager warning: last_user_time (11491292) is greater than comparison timestamp (11491289).  This most likely represents a buggy client sending inaccurate timestamps in messages such as _NET_ACTIVE_WINDOW.  Trying to work around...
Jun 24 13:24:33 galelhiani gnome-shell[1566]: Window manager warning: W10 appears to be one of the offending windows with a timestamp of 11491292.  Working around...
Jun 24 13:26:25 galelhiani pkexec[3117]: pam_unix(polkit-1:session): session opened for user root(uid=0) by (uid=1000)
Jun 24 13:26:25 galelhiani pkexec[3117]: galelhiani: Executing command [USER=root] [TTY=unknown] [CWD=/home/galelhiani] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Jun 24 13:30:01 galelhiani CRON[3148]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 13:30:01 galelhiani CRON[3149]: (root) CMD ([ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi)
Jun 24 13:30:01 galelhiani CRON[3148]: pam_unix(cron:session): session closed for user root
Jun 24 13:32:40 galelhiani systemd[1]: Started Run anacron jobs.
Jun 24 13:32:40 galelhiani anacron[3151]: Anacron 2.3 started on 2026-06-24
Jun 24 13:32:40 galelhiani anacron[3151]: Normal exit (0 jobs run)
Jun 24 13:32:40 galelhiani systemd[1]: anacron.service: Deactivated successfully.
Jun 24 13:35:54 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:35:54 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:40:09 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.78' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 13:40:09 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 13:40:10 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 13:40:10 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 13:40:10 galelhiani gnome-shell[1566]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 13:40:12 galelhiani gdm-password][3175]: gkr-pam: unlocked login keyring
Jun 24 13:40:12 galelhiani NetworkManager[845]: <info>  [1782308412.6025] agent-manager: agent[c55aec3664f740db,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 13:40:12 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 13:40:12 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 13:40:12 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.125' (uid=1000 pid=3180 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 13:40:12 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 13:40:12 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 13:40:12 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 13:40:12 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 13:40:40 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 13:45:42 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:45:42 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:46:06 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.78' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 13:46:06 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 13:46:06 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 13:46:06 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 13:46:06 galelhiani gnome-shell[1566]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 13:46:09 galelhiani gdm-password][3268]: gkr-pam: unlocked login keyring
Jun 24 13:46:09 galelhiani NetworkManager[845]: <info>  [1782308769.2552] agent-manager: agent[8ec0d7537e3b1762,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 13:46:09 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 13:46:09 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 13:46:09 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.130' (uid=1000 pid=3273 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 13:46:09 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 13:46:09 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 13:46:09 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 13:46:36 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 13:51:27 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:51:27 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 13:57:26 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.78' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 13:57:26 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 13:57:26 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 13:57:26 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 13:57:26 galelhiani gnome-shell[1566]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 13:57:28 galelhiani gdm-password][3348]: gkr-pam: unlocked login keyring
Jun 24 13:57:29 galelhiani NetworkManager[845]: <info>  [1782309449.0082] agent-manager: agent[558fbcbcb04df767,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 13:57:29 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 13:57:29 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 13:57:29 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.135' (uid=1000 pid=3353 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 13:57:29 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 13:57:29 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 13:57:29 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 13:57:29 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 13:57:56 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 14:00:25 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.gedit' requested by ':1.43' (uid=1000 pid=1684 comm="/usr/bin/nautilus --gapplication-service " label="unconfined")
Jun 24 14:00:25 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.gedit'
Jun 24 14:00:25 galelhiani gnome-shell[1566]: meta_window_set_stack_position_no_sync: assertion 'window->stack_position >= 0' failed
Jun 24 14:00:28 galelhiani gsd-color[1720]: unable to get EDID for xrandr-Virtual-1: unable to get EDID for output
Jun 24 14:00:49 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:00:49 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:00:50 galelhiani gnome-shell[1566]: libinput error: event1  - Apple Inc. Virtual USB Keyboard: client bug: event processing lagging behind by 33ms, your system is too slow
Jun 24 14:05:55 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 14:05:55 galelhiani update-notifier[2147]: gtk_widget_get_scale_factor: assertion 'GTK_IS_WIDGET (widget)' failed
Jun 24 14:15:53 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:15:53 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:15:54 galelhiani dbus-daemon[844]: [system] Activating via systemd: service name='net.reactivated.Fprint' unit='fprintd.service' requested by ':1.78' (uid=1000 pid=1566 comm="/usr/bin/gnome-shell " label="unconfined")
Jun 24 14:15:54 galelhiani systemd[1]: Starting Fingerprint Authentication Daemon...
Jun 24 14:15:54 galelhiani dbus-daemon[844]: [system] Successfully activated service 'net.reactivated.Fprint'
Jun 24 14:15:54 galelhiani systemd[1]: Started Fingerprint Authentication Daemon.
Jun 24 14:15:54 galelhiani gnome-shell[1566]: JS ERROR: Failed to initialize fprintd service: Gio.IOErrorEnum: GDBus.Error:net.reactivated.Fprint.Error.NoSuchDevice: No devices available
                                              asyncCallback@resource:///org/gnome/gjs/modules/core/overrides/Gio.js:114:23
Jun 24 14:15:58 galelhiani gdm-password][3472]: gkr-pam: unlocked login keyring
Jun 24 14:15:58 galelhiani NetworkManager[845]: <info>  [1782310558.2074] agent-manager: agent[79ffcc8359eee9bd,:1.78/org.gnome.Shell.NetworkAgent/1000]: agent registered
Jun 24 14:15:58 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for software-update-available
Jun 24 14:15:58 galelhiani ubuntu-appindicators@ubuntu.com[1566]: unable to update icon for livepatch
Jun 24 14:15:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Activating service name='org.gnome.ArchiveManager1' requested by ':1.142' (uid=1000 pid=3477 comm="gjs /usr/share/gnome-shell/extensions/ding@rasters" label="unconfined")
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 35 with keysym 35 (keycode e).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 37 with keysym 37 (keycode 10).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 38 with keysym 38 (keycode 11).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 39 with keysym 39 (keycode 12).
Jun 24 14:15:58 galelhiani gnome-shell[1566]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
Jun 24 14:15:58 galelhiani dbus-daemon[1474]: [session uid=1000 pid=1474] Successfully activated service 'org.gnome.ArchiveManager1'
Jun 24 14:15:58 galelhiani gnome-shell[1566]: DING: Detected async api for thumbnails
Jun 24 14:15:58 galelhiani gnome-shell[1566]: DING: GNOME nautilus 42.6
Jun 24 14:16:24 galelhiani systemd[1]: fprintd.service: Deactivated successfully.
Jun 24 14:16:25 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:16:25 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:16:38 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:16:38 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:17:01 galelhiani CRON[3535]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
Jun 24 14:17:01 galelhiani CRON[3536]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Jun 24 14:17:01 galelhiani CRON[3535]: pam_unix(cron:session): session closed for user root
Jun 24 14:18:51 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:18:51 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:20:00 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:20:00 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:21:17 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:21:17 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
Jun 24 14:21:31 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/xdg-ubuntu/parcellite/parcelliterc'
Jun 24 14:21:31 galelhiani parcellite-startup.desktop[1942]: Looking in '/etc/xdg/parcellite/parcelliterc'
