#
# This file generates the sidebar/toctree for all RobotPy projects and should
# be copied to each project when it is updated
#

import os


def write_if_changed(fname, contents):

    try:
        with open(fname, "r") as fp:
            old_contents = fp.read()
    except:
        old_contents = ""

    if old_contents != contents:
        with open(fname, "w") as fp:
            fp.write(contents)


def generate_sidebar(conf, conf_api):

    # determine 'latest' or 'stable'
    # if not conf.do_gen:
    do_gen =  conf["on_rtd"] # os.environ.get("SIDEBAR", None) == "1"
    version = conf["rtd_version"]

    lines = ["", ".. DO NOT MODIFY! THIS PAGE IS AUTOGENERATED!", ""]

    def toctree(name):
        lines.extend(
            [".. toctree::", "    :caption: %s" % name, "    :maxdepth: 2", ""]
        )

    def endl():
        lines.append("")

    def write(project, desc, link):
        if project == conf["subproject"] :
            lines.append("    %s" % link)
        else:
            if project == "external" :
                args = (
                    desc,
                    link,
                )
            elif project == "main":
                args = (
                    desc,
                    "http://docs.openimis.org/en/%s/%s.html" % (version, link),
                )
            else:
                args = (
                    desc,
                    "http://docs.openimis.org/projects/en/%s/%s/%s.html" % (project, version, link),
                )
            lines.append("    %s <%s>" % args)

    toctree("OpenIMIS")
    write("User manual","openIMIS User documentation","index_local")
    write("external","openIMIS Install documentation","https://openimis.atlassian.net/wiki/spaces/OP/pages/906526894")
    write("external","open a ticket", "https://openimis.atlassian.net/servicedesk/customer/portals")
    write("external","openIMIS Wiki", "https://openimis.atlassian.net/wiki/spaces/OP/overview")

    # write("Install","openIMIS Install documentation","index_local")
    
    endl()
    endl()

    """ 
    toctree("User documentation")
    write("main","Users and logins","/user_manual/user_login/user_login")
    write("main","Claims","/user_manual/claims/claims")
    write("main","Administration of registers","/user_manual/register/register")
    write("main","Groups/Families, Insurees and Policies","/user_manual/insuree_policies/insuree_policies")
    write("main","Tools","/user_manual/tools/tools")
    write("main","Offline mode","/user_manual/offline/offline")
    endl()
    endl()


    toctree("AR IMIS user documentation")

    write("main","Concept","/ar_manual/concept")
    write("main","Dimensions","/ar_manual/dimensions")
    write("main","Facts","/ar_manual/facts")
    write("main","Access Data","/ar_manual/access_data")  
    endl()
    endl()
    toctree("Installation documentation")
    write("Install","Minimun Requirement","/net_install/minimum_requirements")
    write("Install","SQL server","/net_install/database_sql_server_installation_guide")
    write("Install","Web application","/net_install/web_app_vb_installation_guide")
    write("Install","Web Service","/net_install/web_service_vb_installation_guide")
    write("Install","Windows service","/net_install/windows_services_installation_guide")
    write("Install","Mobile application","/net_install/mobile_applications_configuration")
    endl()
    endl()

    toctree("AR IMIS installation documentation")
    write("Install","prerequisites","/ar_install/prerequisites")
    write("Install","ar_database_install","/ar_install/ar_database_install")
    write("Install","ar_ssis_install","/ar_install/ar_ssis_install")
    write("Install","r_ssas_install","/ar_install/ar_ssas_install")
    write("Install","ar_iis_install","/ar_install/ar_iis_install")
    write("Install","ar_ssrs_start","/ar_install/ar_ssrs_install")
    write("Install","ar_iis_start","/ar_install/ar_ssis_start")
    endl()
    endl() """


    write_if_changed("_sidebar.rst.inc", "\n".join(lines))